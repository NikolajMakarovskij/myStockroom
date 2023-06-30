import datetime
from django.conf import settings
from device.models import Device
from consumables.models import Consumables, Accessories
from .models import Stockroom, Stock_cat, History, StockAcc,CategoryAcc, HistoryAcc, StockDev, CategoryDev, HistoryDev 



class Stock(object):


    #Общие
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

    def save(self):
        # Обновление сессии 
        self.session[settings.STOCK_SESSION_ID] = self.stock
        self.session.modified = True

    #Расходники
    def get_device(consumable_id):
        """Получение устройства"""
        con_device = list(Consumables.objects.get(id=consumable_id).device.all().distinct())
        list_device = []
        list_id = []
        devices = ''
        if con_device:
            for device in con_device:
                list_device.append(device.name)
                list_id.append(device.id)
        else:
            devices = 'Нет'
        for devices in list_device:
                devices = ', '.join(list_device)
        return devices

    def add_category(consumable_id):
        """Получение категории"""
        if not Consumables.objects.get(id = consumable_id).categories:
            consumable_category = None
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

    def create_history(consumable_id, device_id, quantity, username, status_choise):
        """Создание записи в истории расходников"""
        if not (Stock.add_category(consumable_id)) and (not device_id):
            history = History.objects.create(
                consumable=Consumables.objects.get(id = consumable_id).name, 
                consumableId=Consumables.objects.get(id = consumable_id).id, 
                score = quantity,
                dateInstall = datetime.date.today(),
                user = username,
                status = status_choise
            )
        elif not (Stock.add_category(consumable_id)):
            history = History.objects.create(
                consumable=Consumables.objects.get(id = consumable_id).name, 
                consumableId=Consumables.objects.get(id = consumable_id).id,
                device=Device.objects.filter(id = device_id).get().name, 
                deviceId=Device.objects.filter(id = device_id).get().id, 
                score = quantity,
                dateInstall = datetime.date.today(),
                user = username,
                status = status_choise
            )
        elif not device_id:
            history = History.objects.create(
                consumable=Consumables.objects.get(id = consumable_id).name, 
                consumableId=Consumables.objects.get(id = consumable_id).id,
                score = quantity,
                dateInstall = datetime.date.today(),
                categories = Stock.add_category(consumable_id),
                user = username,
                status = status_choise
            )
        else:
            history = History.objects.create(
                consumable=Consumables.objects.get(id = consumable_id).name, 
                consumableId=Consumables.objects.get(id = consumable_id).id, 
                device=Device.objects.filter(id = device_id).get().name, 
                deviceId=Device.objects.filter(id = device_id).get().id, 
                score = quantity,
                dateInstall = datetime.date.today(),
                categories = Stock.add_category(consumable_id),
                user = username,
                status = status_choise
            )
        return history

    def add_consumable(self, consumable, quantity=1, number_rack=1, number_shelf=1, username=None):
        """
        Добавить расходник на склад или обновить его количество.
        """
        consumable_id = str(consumable.id)
        consumable_score = int(str(consumable.score))
        consumable_add = Consumables.objects.get(id = consumable_id)
        device_id = None
        if Stockroom.objects.filter(consumables = consumable_id):
            consumable_score += quantity 
            Consumables.objects.filter(id = consumable_id).update(score = consumable_score)
            Stockroom.objects.filter(consumables = consumable_id).update(
                dateAddToStock = datetime.date.today(),
                device = Stock.get_device(consumable_id)
            )
        else:
            if Stock.add_category(consumable_id) is None:
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
        Stock.create_history(consumable_id, device_id, quantity, username, status_choise='Приход')
        self.save()

    def remove_consumable(self, consumable, quantity=0, username=None):
        """
        Удаление расходника со склада
        """
        device_id = None
        consumable_id = str(consumable.id)
        if Stockroom.objects.filter(consumables = consumable_id):
            Stockroom.objects.filter(consumables = consumable_id).delete()
            Stock.create_history(consumable_id,device_id, quantity, username, status_choise='Удаление')
        self.save()

    def device_add_consumable(self, consumable, device, quantity=1, username=None):
        """
        Установка расходника в устройство
        """
        device_id = str(device)
        consumable_id = str(consumable.id)
        consumable_score = int(str(consumable.score))
        consumable_score -= quantity 

        Consumables.objects.filter(id = consumable_id).update(score = consumable_score)
        Stockroom.objects.filter(consumables = consumable_id).update(dateInstall = datetime.date.today())
        Stock.create_history(consumable_id, device_id, quantity, username, status_choise='Расход')
        self.save()


    #Комплектующие
    def get_device_acc(consumable_id):
        """Получение устройства"""
        acc_device = list(Accessories.objects.get(id=consumable_id).device.all().distinct())
        list_device = []
        list_id = []
        devices = ''
        if acc_device:
            for device in acc_device:
                list_device.append(device.name)
                list_id.append(device.id)
        else:
            devices = 'Нет'
        for devices in list_device:
                devices = ', '.join(list_device)
        return devices

    def add_category_acc(accessories_id):
        """Получение категории"""
        if not Accessories.objects.get(id = accessories_id).categories:
            accessories_category = 'None'
        else:
            accessories_category = Accessories.objects.get(id = accessories_id).categories.name
            if CategoryAcc.objects.filter(name=accessories_category):
                accessories_category = CategoryAcc.objects.get(name=accessories_category)
            else:
                accessories_category = CategoryAcc.objects.create(
                    name=Accessories.objects.get(id = accessories_id).categories.name,
                    slug=Accessories.objects.get(id = accessories_id).categories.slug
                    )
        return accessories_category


    def create_history_acc(accessories_id, device_id, quantity, username, status_choise):
        """Создание записи в истории комплектующих"""
        if not (Stock.add_category_acc(accessories_id)) and (not device_id):
            history = HistoryAcc.objects.create(
                accessories=Accessories.objects.get(id = accessories_id).name, 
                accessoriesId=Accessories.objects.get(id = accessories_id).id, 
                score = quantity,
                dateInstall = datetime.date.today(),
                user = username,
                status = status_choise
            )
        elif not (Stock.add_category_acc(accessories_id)):
            history = HistoryAcc.objects.create(
                accessories=Accessories.objects.get(id = accessories_id).name, 
                accessoriesId=Accessories.objects.get(id = accessories_id).id,
                device=Device.objects.filter(id = device_id).get().name, 
                deviceId=Device.objects.filter(id = device_id).get().id, 
                score = quantity,
                dateInstall = datetime.date.today(),
                user = username,
                status = status_choise
            )
        elif not device_id:
            history = HistoryAcc.objects.create(
                accessories=Accessories.objects.get(id = accessories_id).name, 
                accessoriesId=Accessories.objects.get(id = accessories_id).id,
                score = quantity,
                dateInstall = datetime.date.today(),
                categories = Stock.add_category_acc(accessories_id),
                user = username,
                status = status_choise
            )
        else:
            history = HistoryAcc.objects.create(
                accessories=Accessories.objects.get(id = accessories_id).name, 
                accessoriesId=Accessories.objects.get(id = accessories_id).id, 
                device=Device.objects.filter(id = device_id).get().name, 
                deviceId=Device.objects.filter(id = device_id).get().id, 
                score = quantity,
                dateInstall = datetime.date.today(),
                categories = Stock.add_category_acc(accessories_id),
                user = username,
                status = status_choise
            )
        return history

    def add_accessories(self, accessories, quantity=1, number_rack=1, number_shelf=1, username=None):
        """
        Добавить комплектующее на склад или обновить его количество.
        """
        accessories_id = str(accessories.id)
        accessories_score = int(str(accessories.score))
        accessories_add = Accessories.objects.get(id = accessories_id)
        device_id = None
        if StockAcc.objects.filter(accessories = accessories_id):
            accessories_score += quantity 
            Accessories.objects.filter(id = accessories_id).update(score = accessories_score)
            StockAcc.objects.filter(accessories = accessories_id).update(
                dateAddToStock = datetime.date.today(),
                device = Stock.get_device_acc(accessories_id)
            )
        else:
            if Stock.add_category_acc(accessories_id) is None:
                StockAcc.objects.create(
                                        accessories = accessories_add,
                                        dateAddToStock = datetime.date.today(),
                                        rack=int(number_rack),
                                        shelf=int(number_shelf),
                                        device = Stock.get_device_acc(accessories_id)
                )
                Accessories.objects.filter(id = accessories_id).update(score = int(quantity))
            else:
                StockAcc.objects.create(
                                        accessories = accessories_add,
                                        categories = Stock.add_category_acc(accessories_id),
                                        dateAddToStock = datetime.date.today(),
                                        rack=int(number_rack),
                                        shelf=int(number_shelf),
                                        device = Stock.get_device_acc(accessories_id)
                )
                Accessories.objects.filter(id = accessories_id).update(score = int(quantity))
        Stock.create_history_acc(accessories_id, device_id, quantity, username, status_choise='Приход')
        self.save()



    def remove_accessories(self, accessories, quantity=0, username=None):
        """
        Удаление комплектующего со склада
        """
        device_id = None
        accessories_id = str(accessories.id)
        if StockAcc.objects.filter(accessories = accessories_id):
            StockAcc.objects.filter(accessories = accessories_id).delete()
            Stock.create_history_acc(accessories_id,device_id, quantity, username, status_choise='Удаление')
        self.save()

    def device_add_accessories(self, accessories, device, quantity=1, username=None):
        """
        Установка расходника в устройство
        """
        device_id = str(device)
        accessories_id = str(accessories.id)
        accessories_score = int(str(accessories.score))
        accessories_score -= quantity 

        Accessories.objects.filter(id = accessories_id).update(score = accessories_score)
        StockAcc.objects.filter(accessories = accessories_id).update(dateInstall = datetime.date.today())
        Stock.create_history_acc(accessories_id, device_id, quantity, username, status_choise='Расход')

        self.save()


    #устройства
    def add_category_dev(device_id):
        """Получение категории"""
        if not Device.objects.get(id = device_id).categories:
            device_category = 'None'
        else:
            device_category = Device.objects.get(id = device_id).categories.name
            if CategoryDev.objects.filter(name=device_category):
                device_category = CategoryDev.objects.get(name=device_category)
            else:
                device_category = CategoryDev.objects.create(
                    name=Device.objects.get(id = device_id).categories.name,
                    slug=Device.objects.get(id = device_id).categories.slug
                    )
        return device_category


    def create_history_dev(device_id, quantity, username, status_choise):
        """Создание записи в истории устройств"""
        if not (Stock.add_category_dev(device_id)):
            history = HistoryDev.objects.create(
                device=Device.objects.get(id = device_id).name, 
                deviceId=Device.objects.get(id = device_id).id, 
                score = quantity,
                dateInstall = datetime.date.today(),
                user = username,
                status = status_choise
            )
        else:
            history = HistoryDev.objects.create(
                device=Device.objects.filter(id = device_id).get().name, 
                deviceId=Device.objects.filter(id = device_id).get().id, 
                score = quantity,
                dateInstall = datetime.date.today(),
                categories = Stock.add_category_acc(device_id),
                user = username,
                status = status_choise
            )
        return history

    def add_device(self, device, quantity=1, number_rack=1, number_shelf=1, username=None):
        """
        Добавить устройство на склад или обновить его количество.
        """
        device_id = str(device.id)
        device_score = int(str(device.score))
        device_add = Device.objects.get(id = device_id)
        if StockDev.objects.filter(devicies = device_id):
            device_score += quantity 
            Device.objects.filter(id = device_id).update(score = device_score)
            StockDev.objects.filter(devicies = device_id).update(
                dateAddToStock = datetime.date.today(),
            )
        else:
            if Stock.add_category_dev(device_id) is None:
                StockDev.objects.create(
                                        devicies = device_add,
                                        dateAddToStock = datetime.date.today(),
                                        rack=int(number_rack),
                                        shelf=int(number_shelf),
                )
                Device.objects.filter(id = device_id).update(score = int(quantity))
            else:
                StockDev.objects.create(
                                        devicies = device_add,
                                        categories = Stock.add_category_dev(device_id),
                                        dateAddToStock = datetime.date.today(),
                                        rack=int(number_rack),
                                        shelf=int(number_shelf),
                )
                Device.objects.filter(id = device_id).update(score = int(quantity))
        Stock.create_history_dev(device_id, quantity, username, status_choise='Приход')
        self.save()



    def remove_device(self, device, quantity=0, username=None):
        """
        Удаление устройства со склада
        """
        device_id = str(device.id)
        if StockDev.objects.filter(devicies = device_id):
            StockDev.objects.filter(devicies = device_id).delete()
            Stock.create_history_dev(device_id, quantity, username, status_choise='Удаление')
        self.save()

    def move_device(self, device, quantity=1, username=None):
        """
        Перемещение устройства
        """
        device_id = str(device)
        device_score = int(str(device.score))
        device_score -= quantity 

        Device.objects.filter(id = device_id).update(score = device_score)
        StockDev.objects.filter(devicies = device_id).update(dateInstall = datetime.date.today())
        Stock.create_history_dev(device_id, quantity, username, status_choise='Перемещение')

        self.save()