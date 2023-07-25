import datetime
from django.conf import settings
from device.models import Device
from consumables.models import Accessories
from .models import CategoryAcc, HistoryAcc, CategoryDev, HistoryDev, StockDev


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


class DevStock(BaseStock):
    """Class with stock methods"""
    base_model = Device
    stock_model = StockDev
    stock_category = CategoryDev
    history_model = HistoryDev
    def create_history_device(self, model_id: str, quantity: int, username: str, status_choice: str) -> None:
        """Creating an entry in the history of stock_model"""
        model = self.base_model.objects.get(id=model_id)
        category = BaseStock.add_category(self, model_id)
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


class Stock(BaseStock):
    """Class with stock methods"""
    pass
