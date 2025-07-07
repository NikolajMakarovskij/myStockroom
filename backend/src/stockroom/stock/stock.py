import datetime
from uuid import UUID

from consumables.models import Accessories, Consumables
from device.models import Device
from stockroom.models.accessories import CategoryAcc, HistoryAcc, StockAcc
from stockroom.models.consumables import History, StockCat, Stockroom
from stockroom.models.devices import CategoryDev, HistoryDev, StockDev
from stockroom.stock.base_stock import BaseStock
from workplace.models import Workplace


class ConStock(BaseStock):
    """Class with stockroom consumables methods

    Other parameters:
        base_model (Consumables): _description_
        stock_model (Stockroom): _description_
        stock_category (StockCat): _description_
        history_model (History): _description_
    """

    base_model = Consumables
    stock_model = Stockroom
    stock_category = StockCat
    history_model = History


class AccStock(BaseStock):
    """Class with stockroom accessories methods

    Other parameters:
        base_model (Accessories): _description_
        stock_model (StockAcc): _description_
        stock_category (CategoryAcc): _description_
        history_model (HistoryAcc): _description_
    """

    base_model = Accessories
    stock_model = StockAcc
    stock_category = CategoryAcc
    history_model = HistoryAcc


class DevStock(BaseStock):
    """Class with stockroom device methods

    Other parameters:
        base_model (Device): _description_
        stock_model (StockDev): _description_
        stock_category (CategoryDev): _description_
        history_model (HistoryDev): _description_
    """

    base_model = Device
    stock_model = StockDev
    stock_category = CategoryDev
    history_model = HistoryDev

    @classmethod
    def create_history_device(
        cls, model_id: UUID, quantity: int, username: str, status_choice: str, note: str
    ) -> HistoryDev:
        """Creating an entry in the history of stockroom device model

        Args:
            model_id (UUID): _stockroom model id_
            quantity (int): _description_
            username (str): _getting from session_
            note (str): _description_
            status_choice (str): _description_

        Returns:
            History (HistoryDev): _Adding instance in database_
        """

        model = cls.base_model.objects.get(id=model_id)
        category = cls.add_category(model_id)
        if not note:
            note = ""
        else:
            note = note
        history = cls.history_model.objects.create(  # type: ignore[misc]
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
        cls, model_id: UUID, quantity=1, number_rack=1, number_shelf=1, username=None
    ) -> None:
        """Add a stockroom device to the stock or update it quantity.

        Args:
            model_id (UUID): _stockroom model id_
            quantity (int): _description_
            number_rack (int): _description_
            number_shelf (int): _description_
            username (str): _getting from session_
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
            cls.stock_model.objects.create(  # type: ignore[misc]
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
        cls, model_id: UUID, quantity=0, username=None, status_choice="Удаление"
    ) -> None:
        """Remove device from the stock

        Args:
            model_id (UUID): _stockroom model id_
            quantity (int): _description_
            username (str): _getting from session_
        """

        model_instance = cls.stock_model.objects.filter(stock_model=model_id)
        if model_instance:
            model_instance.delete()
            cls.create_history_device(
                model_id, quantity, username, status_choice, note=""
            )

    @classmethod
    def move_device(
        cls, model_id: UUID, workplace_id: UUID, username=None, note=None
    ) -> None:
        """Move device

        Args:
            model_id (UUID): _stockroom model id_
            workplace_id (UUID): _workplace model id_
            username (str): _description_
            note (str): _getting from session_
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
