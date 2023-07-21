from .stock import Stock
from .models import StockDev, StockAcc, Stockroom
from consumables.models import Accessories, Consumables
from workplace.models import Workplace
import datetime
from celery import shared_task
from device.models import Device


class StockTasks(Stock):
    # Consumables
    @shared_task()
    def add_consumable(consumable: str, quantity=1,
                       number_rack=1, number_shelf=1,
                       username=None) -> None:
        """
        Add a consumable to the stock or update its quantity.
        """
        consumable_id = str(consumable)
        consumable_add = Consumables.objects.get(id=consumable_id)
        consumable_score = int(str(consumable_add.score))
        device_id = None
        if Stockroom.objects.filter(consumables=consumable_id):
            consumable_score += quantity
            Consumables.objects.filter(
                id=consumable_id).update(score=consumable_score)
            Stockroom.objects.filter(
                consumables=consumable_id).update(
                dateAddToStock=datetime.date.today()
            )
        else:
            if Stock.add_category(consumable_id) is None:
                Stockroom.objects.create(
                    consumables=consumable_add,
                    dateAddToStock=datetime.date.today(),
                    rack=int(number_rack),
                    shelf=int(number_shelf),
                )
                Consumables.objects.filter(
                    id=consumable_id).update(score=int(quantity))
            else:
                Stockroom.objects.create(
                    consumables=consumable_add,
                    categories=Stock.add_category(
                        consumable_id),
                    dateAddToStock=datetime.date.today(),
                    rack=int(number_rack),
                    shelf=int(number_shelf),
                )
                Consumables.objects.filter(
                    id=consumable_id).update(score=int(quantity))
        Stock.create_history(consumable_id, device_id, quantity,
                             username, status_choice='Приход')

    @shared_task()
    def remove_consumable(consumable: str, quantity=0,
                          username=None) -> None:
        """
        Remove consumable from the stock
        """
        device_id = None
        consumable_id = str(consumable)
        if Stockroom.objects.filter(consumables=consumable_id):
            Stockroom.objects.filter(consumables=consumable_id).delete()
            Stock.create_history(consumable_id, device_id, quantity,
                                 username, status_choice='Удаление')

    @shared_task()
    def device_add_consumable(consumable: str, device: dict, quantity=1, username=None) -> None:
        """
        Install consumable in the device
        """
        device_id = str(device)
        consumable_id = str(consumable)
        consumable_add = Consumables.objects.get(id=consumable_id)
        consumable_score = int(str(consumable_add.score))
        consumable_score -= quantity

        Consumables.objects.filter(id=consumable_id).update(score=consumable_score)
        Stockroom.objects.filter(consumables=consumable_id).update(dateInstall=datetime.date.today())
        Stock.create_history(consumable_id, device_id, quantity, username, status_choice='Расход')

    # Accessories
    @shared_task()
    def add_accessories(accessories: str, quantity=1, number_rack=1, number_shelf=1, username=None):
        """
        Add an accessories to the stock or update its quantity.
        """
        accessories_id = str(accessories)
        accessories_add = Accessories.objects.get(id=accessories_id)
        accessories_score = int(str(accessories_add.score))
        device_id = None
        if StockAcc.objects.filter(accessories=accessories_id):
            accessories_score += quantity
            Accessories.objects.filter(id=accessories_id).update(score=accessories_score)
            StockAcc.objects.filter(accessories=accessories_id).update(
                dateAddToStock=datetime.date.today(),
            )
        else:
            if Stock.add_category_acc(accessories_id) is None:
                StockAcc.objects.create(
                    accessories=accessories_add,
                    dateAddToStock=datetime.date.today(),
                    rack=int(number_rack),
                    shelf=int(number_shelf),
                )
                Accessories.objects.filter(id=accessories_id).update(score=int(quantity))
            else:
                StockAcc.objects.create(
                    accessories=accessories_add,
                    categories=Stock.add_category_acc(accessories_id),
                    dateAddToStock=datetime.date.today(),
                    rack=int(number_rack),
                    shelf=int(number_shelf),
                )
                Accessories.objects.filter(id=accessories_id).update(score=int(quantity))
        Stock.create_history_acc(accessories_id, device_id, quantity, username, status_choice='Приход')

    @shared_task()
    def remove_accessories(accessories: str, quantity=0, username=None) -> None:
        """
        Delete accessories from the stock
        """
        device_id = None
        accessories_id = str(accessories)
        if StockAcc.objects.filter(accessories=accessories_id):
            StockAcc.objects.filter(accessories=accessories_id).delete()
            Stock.create_history_acc(accessories_id, device_id, quantity, username, status_choice='Удаление')

    @shared_task()
    def device_add_accessories(accessories: str, device: str, quantity=1, username=None) -> None:
        """
        Install accessories in device
        """
        device_id = str(device)
        accessories_id = str(accessories)
        acc = Accessories.objects.get(id=accessories_id)
        accessories_score = int(str(acc.score))
        accessories_score -= quantity

        Accessories.objects.filter(id=accessories_id).update(score=accessories_score)
        StockAcc.objects.filter(accessories=accessories_id).update(dateInstall=datetime.date.today())
        Stock.create_history_acc(accessories_id, device_id, quantity, username, status_choice='Расход')

    # Devices
    @shared_task()
    def add_device(device_id: str, quantity=1, number_rack=1, number_shelf=1, username=None) -> None:
        """
        Add a device to the stock or update its quantity.
        """
        device_add = Device.objects.get(id=device_id)
        device_score = int(str(device_add.score))
        if StockDev.objects.filter(devices=device_id):
            device_score += quantity
            Device.objects.filter(id=device_id).update(score=device_score)
            StockDev.objects.filter(devices=device_id).update(
                dateAddToStock=datetime.date.today(),
            )
        else:
            if Stock.add_category_dev(device_id) is None:
                StockDev.objects.create(
                    devices=device_add,
                    dateAddToStock=datetime.date.today(),
                    rack=int(number_rack),
                    shelf=int(number_shelf),
                )
                Device.objects.filter(id=device_id).update(score=int(quantity))
            else:
                StockDev.objects.create(
                    devices=device_add,
                    categories=Stock.add_category_dev(device_id),
                    dateAddToStock=datetime.date.today(),
                    rack=int(number_rack),
                    shelf=int(number_shelf),
                )
                Device.objects.filter(id=device_id).update(score=int(quantity))
        Stock.create_history_dev(device_id, quantity, username, status_choice='Приход')

    @shared_task()
    def remove_device(device_id: str, quantity=0, username=None, status_choice=None) -> None:
        """
        Delete device from the stock
        """
        status_choice = "Удаление"
        if StockDev.objects.filter(devices=device_id):
            StockDev.objects.filter(devices=device_id).delete()
            Stock.create_history_dev(device_id, quantity, username, status_choice=status_choice)

    @shared_task()
    def move_device(device_id: str, workplace: str, username=None) -> None:
        """
        Move device
        """
        quantity = 1
        Device.objects.filter(id=device_id).update(workplace=Workplace.objects.filter(name=workplace).get())
        StockDev.objects.filter(devices=device_id).update(dateInstall=datetime.date.today())
        Stock.create_history_dev(device_id, quantity, username,
                                 status_choice=f"Перемещение на рабочее место {workplace}"
                                 )
