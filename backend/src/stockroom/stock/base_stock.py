import datetime
from dataclasses import dataclass

from django.conf import settings
from django.db.models import Model

from device.models import Device


@dataclass
class BaseStock(object):
    """Class with stock base methods"""

    base_model: type[Model] = Model
    stock_model: type[Model] = Model
    stock_category: type[Model] = Model
    history_model: type[Model] = Model

    def __init__(
        self,
        request,
    ):
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

    @classmethod
    def add_category(cls, model_id: str) -> Model | None:
        """Getting a category"""
        model = cls.base_model._default_manager.get(id=model_id)
        if not model.categories: # type: ignore[attr-defined]
            category = None
        else:
            model_category = model.categories.name # type: ignore[attr-defined]
            if cls.stock_category._default_manager.filter(name=model_category): 
                category = cls.stock_category._default_manager.get(name=model_category) 
            else:
                category = cls.stock_category._default_manager.create(
                    name=model.categories.name, slug=model.categories.slug # type: ignore[attr-defined]
                )
        return category

    @classmethod
    def create_history(
        cls,
        model_id: str,
        device_id: str,
        quantity: int,
        username: str,
        note: str,
        status_choice: str,
    ) -> Model:
        """Creating an entry in the history of stock_model"""

        model = cls.base_model._default_manager.get(id=model_id)
        category = cls.add_category(model_id)
        if not device_id:
            device_name: str= ""
            device_id = ""
        else:
            device = Device.objects.get(id=device_id)
            device_name = device.name
            device_id = device.id

        history = cls.history_model._default_manager.create(
            stock_model=model.name, # type: ignore[attr-defined]
            stock_model_id=model.id, # type: ignore[attr-defined]
            device=device_name,
            deviceId=device_id,
            quantity=quantity,
            dateInstall=datetime.date.today(),
            categories=category,
            user=username,
            note=note,
            status=status_choice,
        )
        return history

    @classmethod
    def add_to_stock(
        cls, model_id: str, quantity=1, number_rack=1, number_shelf=1, username=""
    ) -> None:
        """
        Add a stock_model to the stock or update its quantity.
        """

        model = cls.base_model._default_manager.get(id=model_id)
        model_instance = cls.base_model._default_manager.filter(id=model_id)
        model_quantity = int(str(model.quantity)) # type: ignore[attr-defined]
        stock_model_instance = cls.stock_model._default_manager.filter(stock_model=model_id)
        device_id = ""
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
            cls.stock_model._default_manager.create(
                stock_model=model,
                categories=categories,
                dateAddToStock=datetime.date.today(),
                rack=int(number_rack),
                shelf=int(number_shelf),
            )
            model_instance.update(quantity=int(quantity))
        cls.create_history(
            model_id, device_id, quantity, username, note="", status_choice="Приход"
        )

    @classmethod
    def remove_from_stock(cls, model_id: str, quantity=0, username="") -> None:
        """
        Remove stock_model from the stock
        """
        device_id = ""
        stock_model = cls.stock_model._default_manager.filter(stock_model=model_id)
        if stock_model:
            stock_model.delete()
            cls.create_history(
                model_id,
                device_id,
                quantity,
                username,
                note="",
                status_choice="Удаление",
            )

    @classmethod
    def add_to_device(
        cls,
        model_id: str,
        device: dict,
        quantity: int = 1,
        note: str = "",
        username: str = "",
    ) -> None:
        """
        Install stock_model in the device
        """
        device_id = str(device)
        model_add = cls.base_model._default_manager.get(id=model_id)
        model_quantity = int(str(model_add.quantity)) # type: ignore[attr-defined]
        device_obj = Device.objects.get(id=device_id)
        device_note = device_obj.note
        history_note = ""
        model_quantity -= quantity

        if not note:
            device_note
            history_note
        else:
            if device_note is None:
                device_note = f"{datetime.date.today()} {note}"
            else:
                device_note = f"{device_note} {datetime.date.today()} {note}"
            history_note = f"{note}"
        # TODO change Device to self.base_model.device
        # TODO fix tests
        Device.objects.filter(id=device_id).update(note=device_note)
        cls.base_model._default_manager.filter(id=model_id).update(
            quantity=model_quantity,
        )
        cls.stock_model._default_manager.filter(stock_model=model_id).update(
            dateInstall=datetime.date.today()
        )
        cls.create_history(
            model_id,
            device_id,
            quantity,
            username,
            history_note,
            status_choice="Расход",
        )
