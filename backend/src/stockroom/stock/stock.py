import datetime

from consumables.models import Accessories, Consumables
from device.models import Device
from stockroom.models.accessories import CategoryAcc, HistoryAcc, StockAcc
from stockroom.models.consumables import History, StockCat, Stockroom
from stockroom.models.devices import CategoryDev, HistoryDev, StockDev
from stockroom.stock.base_stock import BaseStock
from workplace.models import Workplace


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

    @classmethod
    def create_history_device(
        cls, model_id: str, quantity: int, username: str, status_choice: str, note: str
    ) -> HistoryDev:
        """Creating an entry in the history of stock_model"""
        model = cls.base_model.objects.get(id=model_id)
        category = cls.add_category(model_id)
        if not note:
            note = ""
        else:
            note = note
        history = cls.history_model.objects.create(
            stock_model=model.name,
            stock_model_id=model.id,
            quantity=quantity,
            dateInstall=datetime.date.today(),
            categories=category,
            user=username,
            note=note,
            status=status_choice,
        )
        return history

    @classmethod
    def add_to_stock_device(
        cls, model_id: str, quantity=1, number_rack=1, number_shelf=1, username=None
    ) -> None:
        """
        Add a stock_model to the stock or update its quantity.
        """

        model = cls.base_model.objects.get(id=model_id)
        model_instance = cls.base_model.objects.filter(id=model_id)
        model_quantity = int(str(model.quantity))
        stock_model_instance = cls.stock_model.objects.filter(stock_model=model_id)
        category = cls.add_category(model_id)
        if category is None:
            categories = None
        else:
            categories = category

        if stock_model_instance:
            model_quantity += quantity
            model_instance.update(quantity=model_quantity)
            stock_model_instance.update(dateAddToStock=datetime.date.today())
        else:
            cls.stock_model.objects.create(
                stock_model=model,
                categories=categories,
                dateAddToStock=datetime.date.today(),
                rack=int(number_rack),
                shelf=int(number_shelf),
            )
            model_instance.update(quantity=int(quantity))
        cls.create_history_device(
            model_id, quantity, username, status_choice="Приход", note=""
        )

    @classmethod
    def remove_device_from_stock(
        cls, model_id: str, quantity=0, username=None, status_choice="Удаление"
    ) -> None:
        """
        Delete device from the stock
        """
        model_instance = cls.stock_model.objects.filter(stock_model=model_id)
        if model_instance:
            model_instance.delete()
            cls.create_history_device(
                model_id, quantity, username, status_choice, note=""
            )

    @classmethod
    def move_device(
        cls, model_id: str, workplace_id: str, username=None, note=None
    ) -> None:
        """
        Move device
        """
        model_instance = cls.base_model.objects.filter(id=model_id)
        stock_model_instance = cls.stock_model.objects.filter(stock_model=model_id)
        note = note
        quantity = 1
        workplace = Workplace.objects.get(id=workplace_id)
        workplace_name = workplace.name
        model_instance.update(workplace=workplace)
        stock_model_instance.update(dateInstall=datetime.date.today())
        cls.create_history_device(
            model_id,
            quantity,
            username,
            status_choice=f"Перемещение на рабочее место {workplace_name}",
            note=note,
        )
