from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.forms import widgets
from django.conf import settings
import csv
import datetime
from django.http import HttpResponse

menu = [
    {'title':  "Главная страница", 'url_name': 'index'},
    {'title':  "Раб. места", 'url_name': 'workplace:workplace'},
    {'title':  "Сотрудники", 'url_name': 'employee:employee'},
    {'title':  "Софт", 'url_name': 'software:software'},
    {'title':  "Раб. станции", 'url_name': 'workstation:workstation'},
    {'title':  "Принтеры", 'url_name': 'printer:printer'},
    {'title':  "ЭЦП", 'url_name': 'signature:signature'},
    {'title':  "Справочники", 'url_name': 'references'},
    #{'title':  "Склад", 'url_name': 'warehouse'},
    {'title':  "Расходники", 'url_name': 'consumables:consumables'},
    {'title':  "Контрагенты", 'url_name': 'counterparty:counterparty'},
    #{'title':  "#", 'url_name': '#'},
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
    paginate_by =  10
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        context['query'] = self.request.GET.get('q')
        
        return context

# Кнопка добавить для формы
class WidgetCanAdd(widgets.Select):
    "Отвечает за кнопку добавить в форме для связанных моделей"
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

#Функция экспорта
class ExportAdmin:
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

#отбор значений модели
class ModelMixin:
    def get_all_fields(self):
        """Возвращает список всех полей из записи БД. Используется в шаблонах для DetailView """
        fields = []
        expose_fields = ['id']
        for f in self._meta.fields:

            fname = f.name        
            # resolve picklists/choices, with get_xyz_display() function
            get_choice = 'get_'+fname+'_display'
            if hasattr(self, get_choice):
                value = getattr(self, get_choice)()
            else:
                try:
                    value = getattr(self, fname)
                except AttributeError:
                    value = None

            # only display fields with values and skip some fields entirely
            if f.editable and value and f.name not in (expose_fields) :

                fields.append(
                    {
                    'label':f.verbose_name, 
                    'name':f.name, 
                    'value':value,
                    }
                )
        return fields