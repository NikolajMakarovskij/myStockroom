from device.models import Device
from stockroom.models.accessories import StockAcc, CategoryAcc, HistoryAcc
from stockroom.models.devices import StockDev, CategoryDev, HistoryDev
from stockroom.stock.base_stock import BaseStock
from stockroom.models.consumables import Stockroom, StockCat, History
from consumables.models import Accessories, Consumables
from workplace.models import Workplace
import datetime


class ConStock(BaseStock):
    base_model = Consumables
    stock_model = Stockroom
    stock_category = StockCat
    history_model = History


class AccStock(BaseStock):
    base_model = Accessories
    stock_model = StockAcc
    stock_category = CategoryAcc
    history_model = HistoryAcc


class DevStock(BaseStock):
    base_model = Device
    stock_model = StockDev
    stock_category = CategoryDev
    history_model = HistoryDev

    """Class with stock methods for device"""
    def create_history_device(self, model_id: str, quantity: int, username: str, status_choice: str) -> None:
        """Creating an entry in the history of stock_model"""
        model = self.base_model.objects.get(id=model_id)
        category = self.add_category(self, model_id)
        history = self.history_model.objects.create(
            stock_model=model.name,
            stock_model_id=model.id,
            quantity=quantity,
            dateInstall=datetime.date.today(),
            categories=category,
            user=username,
            status=status_choice
        )
        return history

    def add_to_stock_device(self, model_id: str, quantity=1, number_rack=1, number_shelf=1, username=None) -> None:
        """
        Add a stock_model to the stock or update its quantity.
        """

        model = self.base_model.objects.get(id=model_id)
        model_instance = self.base_model.objects.filter(id=model_id)
        model_quantity = int(str(model.quantity))
        stock_model_instance = self.stock_model.objects.filter(stock_model=model_id)
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

    def remove_device_from_stock(self, model_id: str, quantity=0, username=None, status_choice="Удаление") -> None:
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
