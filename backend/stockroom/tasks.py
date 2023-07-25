from .stock import BaseStock, DevStock
from .models import StockDev, StockAcc, Stockroom, StockCat, History, CategoryAcc, HistoryAcc, CategoryDev, HistoryDev
from consumables.models import Accessories, Consumables
from workplace.models import Workplace
import datetime
from celery import shared_task
from device.models import Device


class BaseStockTasks(BaseStock):
    """
    Class with base tasks of stock methods
    """

    @shared_task()
    def add_to_stock(self, model_id: str, quantity=1, number_rack=1, number_shelf=1, username=None) -> None:
        """
        Add a stock_model to the stock or update its quantity.
        """

        model = self.base_model.objects.get(id=model_id)
        model_instance = self.base_model.objects.filter(id=model_id)
        model_quantity = int(str(model.quantity))
        stock_model_instance = self.stock_model.objects.filter(stock_model=model_id)
        device_id = None
        category = BaseStock.add_category(self, model_id)
        if category is None:
            categories = None
        else:
            categories = category

        if stock_model_instance:
            model_quantity += quantity
            model_instance.update(quantity=model_quantity)
            stock_model_instance.update(dateAddToStock=datetime.date.today())
        else:
            self.stock_model.objects.create(
                stock_model=model,
                categories=categories,
                dateAddToStock=datetime.date.today(),
                rack=int(number_rack),
                shelf=int(number_shelf),
            )
            model_instance.update(quantity=int(quantity))
        BaseStock.create_history(self, model_id, device_id, quantity, username, status_choice='Приход')

    @shared_task()
    def remove_from_stock(self, model_id: str, quantity=0,
                          username=None) -> None:
        """
        Remove stock_model from the stock
        """
        device_id = None
        stock_model = self.stock_model.objects.filter(stock_model=model_id)
        if stock_model:
            stock_model.delete()
            BaseStock.create_history(self, model_id, device_id, quantity,
                                     username, status_choice='Удаление')

    @shared_task()
    def add_to_device(self, model_id: str, device: dict, quantity=1, username=None) -> None:
        """
        Install stock_model in the device
        """
        device_id = str(device)
        model_add = self.base_model.objects.get(id=model_id)
        model_quantity = int(str(model_add.quantity))
        model_quantity -= quantity

        self.base_model.objects.filter(id=model_id).update(quantity=model_quantity)
        self.stock_model.objects.filter(stock_model=model_id).update(dateInstall=datetime.date.today())
        BaseStock.create_history(self, model_id, device_id, quantity, username, status_choice='Расход')


class ConStockTasks(BaseStockTasks):
    base_model = Consumables
    stock_model = Stockroom
    stock_category = StockCat
    history_model = History


class AccStockTasks(BaseStockTasks):
    base_model = Accessories
    stock_model = StockAcc
    stock_category = CategoryAcc
    history_model = HistoryAcc


class DevStockTasks(DevStock):

    @shared_task()
    def add_to_stock_device(self, model_id: str, quantity=1, number_rack=1, number_shelf=1, username=None) -> None:
        """
        Add a stock_model to the stock or update its quantity.
        """

        model = self.base_model.objects.get(id=model_id)
        model_instance = self.base_model.objects.filter(id=model_id)
        model_quantity = int(str(model.quantity))
        stock_model_instance = self.stock_model.objects.filter(stock_model=model_id)
        category = BaseStock.add_category(self, model_id)
        if category is None:
            categories = None
        else:
            categories = category

        if stock_model_instance:
            model_quantity += quantity
            model_instance.update(quantity=model_quantity)
            stock_model_instance.update(dateAddToStock=datetime.date.today())
        else:
            self.stock_model.objects.create(
                stock_model=model,
                categories=categories,
                dateAddToStock=datetime.date.today(),
                rack=int(number_rack),
                shelf=int(number_shelf),
            )
            model_instance.update(quantity=int(quantity))
        DevStock.create_history_device(self, model_id, quantity, username, status_choice='Приход')

    @shared_task()
    def remove_device_from_stock(self, model_id: str, quantity=0, username=None, status_choice=None) -> None:
        """
        Delete device from the stock
        """
        if self.stock_model.objects.filter(stock_model=model_id):
            self.stock_model.objects.filter(stock_model=model_id).delete()
            DevStock.create_history_device(self, model_id, quantity, username, status_choice)

    @shared_task()
    def move_device(self, model_id: str, workplace: str, username=None) -> None:
        """
        Move device
        """
        quantity = 1
        Device.objects.filter(id=model_id).update(workplace=Workplace.objects.filter(name=workplace).get())
        StockDev.objects.filter(stock_model=model_id).update(dateInstall=datetime.date.today())
        DevStock.create_history_device(self, model_id, quantity, username,
                                       status_choice=f"Перемещение на рабочее место {workplace}"
                                       )


class StockTasks(BaseStock):
    pass  # TODO delete class
