from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.forms import widgets
from django.conf import settings

menu = [
    {'title':  "Главная страница", 'url_name': 'index'},
    {'title':  "Раб. места", 'url_name': 'workplace'},
    {'title':  "Сотрудники", 'url_name': 'employee'},
    {'title':  "Софт", 'url_name': 'software'},
    {'title':  "Раб. станции", 'url_name': 'workstation'},
    {'title':  "Принтеры", 'url_name': 'printer'},
    {'title':  "ЭЦП", 'url_name': 'signature'},
    {'title':  "Справочники", 'url_name': 'references'},
    {'title':  "Склад", 'url_name': 'warehouse'},
    {'title':  "Расходники", 'url_name': 'consumables'},
    #{'title':  "Контрагенты", 'url_name': '#'},
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
# button add in form
class WidgetCanAdd(widgets.Select):

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