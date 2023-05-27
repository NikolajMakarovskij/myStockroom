from django.core.cache import cache
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.forms import widgets
from django.conf import settings
from django.contrib import messages
import csv
import datetime
from django.http import HttpResponse

menu = [
    {'title':  "Главная страница", 'url_name': 'catalog:index'},
    {'title':  "Раб. места", 'url_name': 'workplace:workplace_list'},
    {'title':  "Сотрудники", 'url_name': 'employee:employee_list'},
    {'title':  "Софт", 'url_name': 'software:software_list'},
    {'title':  "Раб. станции", 'url_name': 'workstation:workstation_list'},
    {'title':  "Принтеры", 'url_name': 'printer:printer_list'},
    {'title':  "ЭЦП", 'url_name': 'signature:signature_list'},
    {'title':  "Справочники", 'url_name': 'catalog:references_list'},
    {'title':  "Склад", 'url_name': 'stockroom:stock_list'},
    {'title':  "Расходники", 'url_name': 'consumables:consumables_list'},
    {'title':  "Контрагенты", 'url_name': 'counterparty:counterparty'},
    ]
workstationMenu = [
    {'title':  "Информация о системе", 'anchor': '#systemInfo'},
    {'title':  "Информация об ОС", 'anchor': '#OSInfo'},
    {'title':  "Информация о сотруднике", 'anchor': '#infoEmployee'},
    {'title':  "Монитор", 'anchor': '#monitor'},
    {'title':  "Материнская плата", 'anchor': '#motherboard'},
    ]
printerMenu = [
    {'title':  "Информация о принтере", 'anchor': '#printerInfo'},
    {'title':  "Информация о картридже", 'anchor': '#cartridgeInfo'},
    {'title':  "Информация о фотовале", 'anchor': '#fotovalInfo'},
    {'title':  "Информация о тонере", 'anchor': '#tonerInfo'},
    {'title':  "Местоположение", 'anchor': '#workplaceInfo'},
    ]


class DataMixin:
    """
    Миксин с пагинацией, меню, поиском
    """
    paginate_by =  10
    
    def get_user_context(self, **kwargs):
        side_menu = cache.get('side_menu')
        if not side_menu:
            side_menu = menu
            cache.set('side_menu', side_menu, 3000)
        context = kwargs
        context['menu'] = side_menu
        context['query'] = self.request.GET.get('q')
  
        return context


class WidgetCanAdd(widgets.Select):
    """
    Кнопка добавить в форме для связанных моделей
    """
    def __init__(self, related_model, related_url=None, *args, **kw):

        super(WidgetCanAdd, self).__init__(*args, **kw)

        if not related_url:
            rel_to = related_model
            info = (rel_to._meta.app_label, rel_to._meta.object_name.lower())
            related_url = 'admin:%s_%s_add' % info

        # Be careful that here "reverse" is not allowed
        self.related_url = related_url

    def render(self, name, value, *args, **kwargs):
        self.related_url = reverse_lazy(self.related_url)
        output = [super(WidgetCanAdd, self).render(name, value, *args, **kwargs)]
        output.append('<a href="%s" class="add-another" id="add_id_%s" onclick="return showAddAnotherPopup(this);"> ' % \
            (self.related_url, name))
        output.append('<img src="%simages/add.svg" width="35" height="35" alt="%s"/></a>' % (settings.STATIC_URL, '+'))
        return mark_safe(''.join(output))


class ExportAdmin:
    """
    Функция экспорта в админке
    """
    def export_to_csv(modeladmin, request, queryset):
        opts = modeladmin.model._meta
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts.verbose_name)
        writer = csv.writer(response)
        fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
        # Write a first row with header information
        writer.writerow([field.verbose_name for field in fields])
        # Write data rows
        for obj in queryset:
            data_row = []
            for field in fields:
                value = getattr(obj, field.name)
                if isinstance(value, datetime.datetime):
                    value = value.strftime('%d/%m/%Y')
                data_row.append(value)
            writer.writerow(data_row)
        return response
    export_to_csv.short_description = 'экспорт CSV'
    class Meta:
        verbose_name = 'экспорт CSV'
        verbose_name_plural = 'экспорт CSV'


class ModelMixin:
    """
    Миксин с функциями для моделей
    """
    def get_all_fields(self):
        """
        Возвращает список всех полей из записи БД. Используется в шаблонах для DetailView
        """
        fields = []
        expose_fields = ['id', 'slug']
        for f in self._meta.fields:

            fname = f.name        
            # Разрешает списки выбора с помощью get_xyz_display() 
            get_choice = 'get_'+fname+'_display'
            if hasattr(self, get_choice):
                value = getattr(self, get_choice)()
            else:
                try:
                    value = getattr(self, fname)
                except AttributeError:
                    value = None

            # Отображение полей всех полей, кроме исключенных
            if f.editable and value and f.name not in (expose_fields) :

                fields.append(
                    {
                    'label':f.verbose_name, 
                    'name':f.name, 
                    'value':value,
                    }
                )
        return fields

class FormMessageMixin:
    """
    Добавляет сообщения в формы
    """
    success_message = ''
    debug_message = ''
    info_message = ''
    warning_message = ''
    error_message = ''
    success_url = ''

    def form_valid(self, form):
        response = super().form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        debug_message = self.get_debug_message(form.cleaned_data)
        info_message = self.get_info_message(form.cleaned_data)
        warning_message = self.get_warning_message(form.cleaned_data)
        error_message = self.get_error_message(form.cleaned_data)
        if not response:
            if error_message:
                messages.error(self.request, error_message)
        else:
            if success_message:
                messages.debug(self.request, debug_message)
            if info_message:
                messages.info(self.request, info_message)
            if success_message:
                messages.success(self.request, success_message)
            if warning_message:
                messages.warning(self.request, warning_message)
        return response 

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data
    
    def get_debug_message(self, cleaned_data):
        return self.debug_message % cleaned_data
    
    def get_info_message(self, cleaned_data):
        return self.info_message % cleaned_data
    
    def get_warning_message(self, cleaned_data):
        return self.warning_message % cleaned_data
    
    def get_error_message(self, cleaned_data):
        return self.error_message % cleaned_data
    