menu = [
    {'title':  "Главная страница", 'url_name': 'index'},
    {'title':  "Раб. места", 'url_name': 'workplace'},
    {'title':  "Сотрудники", 'url_name': 'employee'},
    {'title':  "Софт", 'url_name': 'software'},
    {'title':  "Раб. станции", 'url_name': 'workstation'},
    {'title':  "Принтеры", 'url_name': 'printer'},
    {'title':  "ЭЦП", 'url_name': 'digital-signature'},
    #{'title':  "Склад", 'url_name': '#'},
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
    {'title':  "Информация о бумаге", 'anchor': '#paperInfo'},
    {'title':  "Местоположение", 'anchor': '#workplaceInfo'},
    ]

class DataMixin:
    paginate_by =  10
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        context['query'] = self.request.GET.get('q')
        
        return context