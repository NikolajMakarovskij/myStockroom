from .stock import BaseStock, DevStock
from .models import StockAcc, Stockroom, StockCat, History, CategoryAcc, HistoryAcc
from consumables.models import Accessories, Consumables
from workplace.models import Workplace
import datetime


class BaseStockTasks(BaseStock):
    """
    Class with base tasks of stock methods
    """

    def add_to_stock(self, model_id: str, quantity=1, number_rack=1, number_shelf=1, username=None) -> None:
        """
        Add a stock_model to the stock or update its quantity.
        """

        model = self.base_model.objects.get(id=model_id)
        model_instance = self.base_model.objects.filter(id=model_id)
        model_quantity = int(str(model.quantity))
        stock_model_instance = self.stock_model.objects.filter(stock_model=model_id)
        device_id = None
        category = self.add_category(self, model_id)
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
        self.create_history(self, model_id, device_id, quantity, username, status_choice='Приход')

    def remove_from_stock(self, model_id: str, quantity=0, username=None) -> None:
        """
        Remove stock_model from the stock
        """
        device_id = None
        stock_model = self.stock_model.objects.filter(stock_model=model_id)
        if stock_model:
            stock_model.delete()
            self.create_history(self, model_id, device_id, quantity,
                                username, status_choice='Удаление')

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
        self.create_history(self, model_id, device_id, quantity, username, status_choice='Расход')


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

    def add_to_stock_device(self, model_id: str, quantity=1, number_rack=1, number_shelf=1, username=None) -> None:
        """
        Add a stock_model to the stock or update its quantity.
        """

        model = self.base_model.objects.get(id=model_id)
        model_instance = self.base_model.objects.filter(id=model_id)
        model_quantity = int(str(model.quantity))
        stock_model_instance = DevStock.stock_model.objects.filter(stock_model=model_id)
        category = self.add_category(self, model_id)
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
        self.create_history_device(self, model_id, quantity, username, status_choice='Приход')

    def remove_device_from_stock(self, model_id: str, quantity=0, username=None, status_choice=None) -> None:
        """
        Delete device from the stock
        """
        model_instance = self.stock_model.objects.filter(stock_model=model_id)
        if model_instance:
            model_instance.delete()
            self.create_history_device(self, model_id, quantity, username, status_choice)

    def move_device(self, model_id: str, workplace: str, username=None) -> None:
        """
        Move device
        """
        model_instance = self.base_model.objects.filter(id=model_id)
        stock_model_instance = self.stock_model.objects.filter(stock_model=model_id)
        quantity = 1
        model_instance.update(workplace=Workplace.objects.filter(name=workplace).get())
        stock_model_instance.update(dateInstall=datetime.date.today())
        self.create_history_device(self, model_id, quantity, username,
                                   status_choice=f"Перемещение на рабочее место {workplace}"
                                   )
