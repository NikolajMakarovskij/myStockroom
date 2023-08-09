import datetime

from django.conf import settings

from device.models import Device


class BaseStock(object):
    """Class with stock base methods"""

    def __init__(self, request, ):
        """
        Initializes the stock
        """
        self.session = request.session
        stock = self.session.get(settings.STOCK_SESSION_ID)
        if not stock:
            stock = self.session[settings.STOCK_SESSION_ID] = {}
        self.stock = stock
        self.base_model = None
        self.stock_model = None
        self.stock_category = None
        self.history_model = None

    def save(self):
        self.session[settings.STOCK_SESSION_ID] = self.stock
        self.session.modified = True

    def add_category(self, model_id: str) -> dict:
        """Getting a category"""
        model = self.base_model.objects.get(id=model_id)
        if not model.categories:
            category = None
        else:
            model_category = (
                model.categories.name
            )
            if self.stock_category.objects.filter(name=model_category):
                category = self.stock_category.objects.get(
                    name=model_category
                )
            else:
                category = self.stock_category.objects.create(
                    name=model.categories.name,
                    slug=model.categories.slug
                )
        return category

    def create_history(self, model_id: str, device_id: str,
                       quantity: int, username: str, status_choice: str
                       ) -> dict:
        """Creating an entry in the history of stock_model"""

        model = self.base_model.objects.get(id=model_id)
        category = BaseStock.add_category(self, model_id)
        if not device_id:
            device_name = None
            device_id = None
        else:
            device = Device.objects.get(id=device_id)
            device_name = device.name
            device_id = device.id

        history = self.history_model.objects.create(
            stock_model=model.name,
            stock_model_id=model.id,
            device=device_name,
            deviceId=device_id,
            quantity=quantity,
            dateInstall=datetime.date.today(),
            categories=category,
            user=username,
            status=status_choice
        )
        return history

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

    def add_to_device(self, model_id: str, device: dict, quantity: int = 1, note: str = None,
                      username: str = None) -> None:
        """
        Install stock_model in the device
        """
        device_id = str(device)
        model_add = self.base_model.objects.get(id=model_id)
        model_quantity = int(str(model_add.quantity))
        model_note = model_add.note
        model_quantity -= quantity
        if not note:
            model_note
        else:
            if model_note is None:
                model_note = f"{note}"
            else:
                model_note = f"{model_note} {note}"

        self.base_model.objects.filter(id=model_id).update(
            quantity=model_quantity,
            note=model_note
        )
        self.stock_model.objects.filter(stock_model=model_id).update(dateInstall=datetime.date.today())
        self.create_history(self, model_id, device_id, quantity, username, status_choice='Расход')
