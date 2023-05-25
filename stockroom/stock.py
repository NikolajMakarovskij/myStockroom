import datetime
from django.conf import settings
from consumables.models import Consumables 
from .models import Stockroom, Stock_cat, History



class Stock(object):

    def __init__(self, request):
        """
        Инициализирует склад
        """
        self.session = request.session
        stock = self.session.get(settings.STOCK_SESSION_ID)
        if not stock:
            # Сохранение пустого склада
            stock = self.session[settings.STOCK_SESSION_ID] = {}
        self.stock = stock

    def add_category(consumable_id):
        """Получение категории из расходников"""
        if not Consumables.objects.get(id = consumable_id).categories:
            consumable_category = 'None'
        else:
            consumable_category = Consumables.objects.get(id = consumable_id).categories.name
            if Stock_cat.objects.filter(name=consumable_category):
                consumable_category = Stock_cat.objects.get(name=consumable_category)
            else:
                consumable_category = Stock_cat.objects.create(
                    name=Consumables.objects.get(id = consumable_id).categories.name,
                    slug=Consumables.objects.get(id = consumable_id).categories.slug
                    )
        return consumable_category

    def create_history(consumable_id, quantity, username, status_choise):
        if Stock.add_category(consumable_id) == 'None':
            history = History.objects.create(
                consumable=Consumables.objects.get(id = consumable_id).name, 
                consumableId=Consumables.objects.get(id = consumable_id).id, 
                score = quantity,
                dateInstall = datetime.date.today(),
                user = username,
                status = status_choise
            )
        else:
            history = History.objects.create(
                consumable=Consumables.objects.get(id = consumable_id).name, 
                consumableId=Consumables.objects.get(id = consumable_id).id, 
                score = quantity,
                dateInstall = datetime.date.today(),
                categories = Stock.add_category(consumable_id),
                user = username,
                status = status_choise
            )
        return history

    def get_device(consumable_id):
        """Получение устройства"""
        con_device = list(Consumables.objects.get(id=consumable_id).device.all().distinct())
        con_ups = list(Consumables.objects.get(id=consumable_id).ups.all().distinct())
        con_cassette = list(Consumables.objects.get(id=consumable_id).cassette.all().distinct())
        list_device = []
        devices = ''
        if con_device:
            for device in con_device:
                list_device.append(device.name)
        elif con_ups and con_cassette:
            for device in con_ups:
                list_device.append(device.name)
            for device in con_cassette:
                list_device.append(device.name)
        elif con_ups:
            for device in con_ups:
                list_device.append(device.name)
        elif con_cassette:
            for device in con_cassette:
                list_device.append(device.name)
        else:
            devices = 'Нет'
        for devices in list_device:
                devices = ', '.join(list_device)
        return devices



    def add_consumable(self, consumable, quantity=1, number_rack=1, number_shelf=1, username=None):
        """
        Добавить расходник на склад или обновить его количество.
        """
        consumable_id = str(consumable.id)
        consumable_score = int(str(consumable.score))
        consumable_add = Consumables.objects.get(id = consumable_id)
        if Stockroom.objects.filter(consumables = consumable_id):
            consumable_score += quantity 
            Consumables.objects.filter(id = consumable_id).update(score = consumable_score)
            Stockroom.objects.filter(consumables = consumable_id).update(
                dateAddToStock = datetime.date.today(),
                device = Stock.get_device(consumable_id)
            )
        else:
            if Stock.add_category(consumable_id) == 'None':
                Stockroom.objects.create(
                                        consumables = consumable_add,
                                        dateAddToStock = datetime.date.today(),
                                        rack=int(number_rack),
                                        shelf=int(number_shelf),
                                        device = Stock.get_device(consumable_id)
                )
                Consumables.objects.filter(id = consumable_id).update(score = int(quantity))
            else:
                Stockroom.objects.create(
                                        consumables = consumable_add,
                                        categories = Stock.add_category(consumable_id),
                                        dateAddToStock = datetime.date.today(),
                                        rack=int(number_rack),
                                        shelf=int(number_shelf),
                                        device = Stock.get_device(consumable_id)
                )
                Consumables.objects.filter(id = consumable_id).update(score = int(quantity))
        Stock.create_history(consumable_id, quantity, username, status_choise='Приход')
        
        
        self.save()

    def save(self):
        # Обновление сессии 
        self.session[settings.STOCK_SESSION_ID] = self.stock
        self.session.modified = True

    def remove_consumable(self, consumable, quantity=0, username=None):
        """
        Удаление картриджа со склада
        """
        consumable_id = str(consumable.id)
        if Stockroom.objects.filter(consumables = consumable_id):
            Stockroom.objects.filter(consumables = consumable_id).delete()
            Stock.create_history(consumable_id, quantity, username, status_choise='Удаление')
        self.save()

    def device_add_consumable(self, consumable, quantity=1, username=None):
        """
        Установка расходника в устройство
        """
        consumable_id = str(consumable.id)
        consumable_score = int(str(consumable.score))
        consumable_score -= quantity 

        Consumables.objects.filter(id = consumable_id).update(score = consumable_score)
        Stockroom.objects.filter(consumables = consumable_id).update(dateInstall = datetime.date.today())
        Stock.create_history(consumable_id, quantity, username, status_choise='Расход')

        self.save()
