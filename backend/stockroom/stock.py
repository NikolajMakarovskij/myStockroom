import datetime
from django.conf import settings
from device.models import Device
from consumables.models import Consumables, Accessories
from workplace.models import Workplace
from .models import StockCat, History, CategoryAcc, HistoryAcc, StockDev, CategoryDev, HistoryDev


class Stock(object):
    """Class with stock methods"""

    # Общие
    def __init__(self, request):
        """
        Initializes the stock
        """
        self.session = request.session
        stock = self.session.get(settings.STOCK_SESSION_ID)
        if not stock:
            stock = self.session[settings.STOCK_SESSION_ID] = {}
        self.stock = stock

    def save(self):
        self.session[settings.STOCK_SESSION_ID] = self.stock
        self.session.modified = True

    # Consumables
    def get_device(consumable_id: str) -> str:
        """Getting a device"""
        con_device = list(
            Consumables.objects.get(id=consumable_id).device.all().distinct()
        )
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

    def add_category(consumable_id: str) -> dict:
        """Getting a category"""
        if not Consumables.objects.get(id=consumable_id).categories:
            consumable_category = None
        else:
            consumable_category = (
                Consumables.objects.get(id=consumable_id).categories.name
            )
            if StockCat.objects.filter(name=consumable_category):
                consumable_category = StockCat.objects.get(
                    name=consumable_category
                )
            else:
                consumable_category = StockCat.objects.create(
                    name=Consumables.objects.get(
                        id=consumable_id).categories.name,
                    slug=Consumables.objects.get(
                        id=consumable_id).categories.slug
                )
        return consumable_category

    def create_history(consumable_id: str, device_id: str,
                       quantity: int, username: str, status_choice: str
                       ) -> dict:
        """Creating an entry in the history of consumables"""
        if not (Stock.add_category(consumable_id)) and (not device_id):
            history = History.objects.create(
                consumable=Consumables.objects.get(id=consumable_id).name,
                consumableId=Consumables.objects.get(id=consumable_id).id,
                score=quantity,
                dateInstall=datetime.date.today(),
                user=username,
                status=status_choice
            )
        elif not (Stock.add_category(consumable_id)):
            history = History.objects.create(
                consumable=Consumables.objects.get(id=consumable_id).name,
                consumableId=Consumables.objects.get(id=consumable_id).id,
                device=Device.objects.filter(id=device_id).get().name,
                deviceId=Device.objects.filter(id=device_id).get().id,
                score=quantity,
                dateInstall=datetime.date.today(),
                user=username,
                status=status_choice
            )
        elif not device_id:
            history = History.objects.create(
                consumable=Consumables.objects.get(id=consumable_id).name,
                consumableId=Consumables.objects.get(id=consumable_id).id,
                score=quantity,
                dateInstall=datetime.date.today(),
                categories=Stock.add_category(consumable_id),
                user=username,
                status=status_choice
            )
        else:
            history = History.objects.create(
                consumable=Consumables.objects.get(id=consumable_id).name,
                consumableId=Consumables.objects.get(id=consumable_id).id,
                device=Device.objects.filter(id=device_id).get().name,
                deviceId=Device.objects.filter(id=device_id).get().id,
                score=quantity,
                dateInstall=datetime.date.today(),
                categories=Stock.add_category(consumable_id),
                user=username,
                status=status_choice
            )
        return history

    # Accessories
    def get_device_acc(accessories_id: str) -> str:
        """Getting a device"""
        acc_device = list(Accessories.objects.get(id=accessories_id).device.all().distinct())
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

    def add_category_acc(accessories_id: str) -> dict:
        """Getting a category"""
        if not Accessories.objects.get(id=accessories_id).categories:
            accessories_category = None
        else:
            accessories_category = Accessories.objects.get(id=accessories_id).categories.name
            if CategoryAcc.objects.filter(name=accessories_category):
                accessories_category = CategoryAcc.objects.get(name=accessories_category)
            else:
                accessories_category = CategoryAcc.objects.create(
                    name=Accessories.objects.get(id=accessories_id).categories.name,
                    slug=Accessories.objects.get(id=accessories_id).categories.slug
                )
        return accessories_category

    def create_history_acc(accessories_id: str, device_id: str, quantity: int, username: str,
                           status_choice: str) -> dict:
        """Creating an entry in the history of accessories"""
        if not (Stock.add_category_acc(accessories_id)) and (not device_id):
            history = HistoryAcc.objects.create(
                accessories=Accessories.objects.get(id=accessories_id).name,
                accessoriesId=Accessories.objects.get(id=accessories_id).id,
                score=quantity,
                dateInstall=datetime.date.today(),
                user=username,
                status=status_choice
            )
        elif not (Stock.add_category_acc(accessories_id)):
            history = HistoryAcc.objects.create(
                accessories=Accessories.objects.get(id=accessories_id).name,
                accessoriesId=Accessories.objects.get(id=accessories_id).id,
                device=Device.objects.filter(id=device_id).get().name,
                deviceId=Device.objects.filter(id=device_id).get().id,
                score=quantity,
                dateInstall=datetime.date.today(),
                user=username,
                status=status_choice
            )
        elif not device_id:
            history = HistoryAcc.objects.create(
                accessories=Accessories.objects.get(id=accessories_id).name,
                accessoriesId=Accessories.objects.get(id=accessories_id).id,
                score=quantity,
                dateInstall=datetime.date.today(),
                categories=Stock.add_category_acc(accessories_id),
                user=username,
                status=status_choice
            )
        else:
            history = HistoryAcc.objects.create(
                accessories=Accessories.objects.get(id=accessories_id).name,
                accessoriesId=Accessories.objects.get(id=accessories_id).id,
                device=Device.objects.filter(id=device_id).get().name,
                deviceId=Device.objects.filter(id=device_id).get().id,
                score=quantity,
                dateInstall=datetime.date.today(),
                categories=Stock.add_category_acc(accessories_id),
                user=username,
                status=status_choice
            )
        return history

    # Devices
    def add_category_dev(device_id: str) -> dict:
        """Getting a category"""
        if not Device.objects.get(id=device_id).categories:
            device_category = None
        else:
            device_category = Device.objects.get(id=device_id).categories.name
            if CategoryDev.objects.filter(name=device_category):
                device_category = CategoryDev.objects.get(name=device_category)
            else:
                device_category = CategoryDev.objects.create(
                    name=Device.objects.get(id=device_id).categories.name,
                    slug=Device.objects.get(id=device_id).categories.slug
                )
        return device_category

    def create_history_dev(device_id: str, quantity: int, username: int, status_choice: str) -> None:
        """Creating an entry in the history of devices"""
        if not (Stock.add_category_dev(device_id)):
            history = HistoryDev.objects.create(
                devices=Device.objects.get(id=device_id).name,
                devicesId=Device.objects.get(id=device_id).id,
                score=quantity,
                dateInstall=datetime.date.today(),
                user=username,
                status=status_choice
            )
        else:
            history = HistoryDev.objects.create(
                devices=Device.objects.filter(id=device_id).get().name,
                devicesId=Device.objects.filter(id=device_id).get().id,
                score=quantity,
                dateInstall=datetime.date.today(),
                categories=Stock.add_category_dev(device_id),
                user=username,
                status=status_choice
            )
        return history
