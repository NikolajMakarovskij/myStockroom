from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget

from dataclasses import dataclass
from device.models import Device
from consumables.models import Consumables, Accessories
from stockroom.models.devices import StockDev, CategoryDev
from stockroom.models.consumables import Stockroom, StockCat, History
from stockroom.models.accessories import StockAcc, CategoryAcc, HistoryAcc

from datetime import datetime


@dataclass
class BaseStockResource(resources.ModelResource):
    """Class with stock base methods"""
    stock_model: dict = None
    stock_category: dict = None

    name = fields.Field(
        column_name='Название',
        attribute='stock_model',
        widget=ForeignKeyWidget(stock_model, field='name')
    )
    categories = fields.Field(
        column_name='Категория',
        attribute='categories',
        widget=ForeignKeyWidget(stock_category, field='name')
    )
    manufacturer = fields.Field(
        column_name='Производитель',
        attribute='stock_model',
        widget=ForeignKeyWidget(stock_model, field='manufacturer__name')
    )
    serial = fields.Field(
        column_name='Серийный номер',
        attribute='stock_model',
        widget=ForeignKeyWidget(stock_model, field='serial')
    )
    serialImg = fields.Field(
        column_name='Фото серийного номера',
        attribute='stock_model',
        widget=ForeignKeyWidget(stock_model, field='serialImg')
    )
    invent = fields.Field(
        column_name='Инвентарный номер',
        attribute='stock_model',
        widget=ForeignKeyWidget(stock_model, field='invent')
    )
    inventImg = fields.Field(
        column_name='Фото инвентарного номера',
        attribute='stock_model',
        widget=ForeignKeyWidget(stock_model, field='inventImg')
    )
    description = fields.Field(
        column_name='Описание',
        attribute='stock_model',
        widget=ForeignKeyWidget(stock_model, field='description')
    )
    quantity = fields.Field(
        column_name='Количество',
        attribute='stock_model',
        widget=ForeignKeyWidget(stock_model, field='quantity')
    )
    note = fields.Field(
        column_name='Примечание',
        attribute='stock_model',
        widget=ForeignKeyWidget(stock_model, field='note')
    )
    dateAddToStock = fields.Field(
        column_name='Дата поступления на склад',
        attribute='dateAddToStock'
    )
    dateInstall = fields.Field(
        column_name="Дата установки",
        attribute='dateInstall'
    )
    rack = fields.Field(
        column_name="Стеллаж",
        attribute='rack'
    )
    shelf = fields.Field(
        column_name="Полка",
        attribute='shelf'
    )


class StockDevResource(BaseStockResource):
    stock_model = Device
    stock_category = CategoryDev

    hostname = fields.Field(
        column_name='Имя хоста',
        attribute='stock_model',
        widget=ForeignKeyWidget(stock_model, field='hostname')
    )
    ip_address = fields.Field(
        column_name='IP адрес',
        attribute='stock_model',
        widget=ForeignKeyWidget(stock_model, field='ip_address')
    )
    workplace = fields.Field(
        column_name='Рабочее место',
        attribute='stock_model',
        widget=ForeignKeyWidget(stock_model, field='workplace__name')
    )

    class Meta:
        model = StockDev
        exclude = ['stock_model']


class StockConResource(BaseStockResource):
    stock_model = Consumables
    stock_category = StockCat

    class Meta:
        model = Stockroom
        exclude = ['stock_model']


class StockAccResource(BaseStockResource):
    stock_model = Accessories
    stock_category = CategoryAcc

    class Meta:
        model = StockAcc
        exclude = ['stock_model']


class ConsumptionResource(resources.ModelResource):
    stock_model = fields.Field(
        column_name="Название",
    )
    devices = fields.Field(
        column_name="Устройства",
    )
    devices_count = fields.Field(
        column_name="Количество устройств",
    )
    quantity_all = fields.Field(
        column_name="Расход за все время",
    )
    quantity_last_year = fields.Field(
        column_name="Расход за прошлый год",
    )
    quantity_current_year = fields.Field(
        column_name="Расход за текущий год",
    )
    quantity = fields.Field(
        column_name='Остаток',
        attribute='quantity',
    )

    def get_queryset(self):
        return self._meta.model.objects.filter(status='Расход').order_by('stock_model').distinct('stock_model')

    class Meta:
        model = History
        exclude = ['id', 'stock_model_id', 'device', 'deviceId', 'categories', 'dateInstall', 'user', 'status', 'note']

    def dehydrate_stock_model(self, history):
        name = getattr(history, "stock_model")
        return name

    def dehydrate_quantity(self, history):
        id = getattr(history, "stock_model_id")
        consumables = Consumables.objects.all()
        if not consumables.filter(id=id):
            quantity = ''
        else:
            quantity = consumables.filter(id=id).get().quantity
        return quantity

    def dehydrate_devices(self, history):
        id = getattr(history, "stock_model_id")
        device_list = []
        consumables = Consumables.objects.all()
        if not consumables.filter(id=id):
            devices = ''
        else:
            consumable = consumables.filter(id=id).get()
            if not consumable.device.all():
                devices = ''
            else:
                devices = consumable.device.all().order_by('name').distinct('name')
                for device in devices:
                    device_list.append(device.name)
                devices = '|'.join(device_list)
        return devices

    def dehydrate_devices_count(self, history):
        id = getattr(history, "stock_model_id")
        consumables = Consumables.objects.all()
        if not consumables.filter(id=id):
            devices_count = ''
        else:
            consumable = consumables.filter(id=id).get()
            if not consumable.device.all():
                devices_count = ''
            else:
                devices_count = consumable.device.count()
        return devices_count

    def dehydrate_quantity_all(self, history):
        quantity_all = 0
        id = getattr(history, "stock_model_id")
        history = History.objects.all()
        unit_history_all = history.filter(
            stock_model_id=id,
            status='Расход',
        )
        for unit in unit_history_all:
            quantity_all += unit.quantity
        return quantity_all

    def dehydrate_quantity_last_year(self, history):
        quantity_last_year = 0
        id = getattr(history, "stock_model_id")
        cur_year = datetime.now()
        history = History.objects.all()
        unit_history_last_year = history.filter(
            stock_model_id=id,
            status='Расход',
            dateInstall__gte=f"{int(cur_year.strftime('%Y')) - 1}-01-01",
            dateInstall__lte=f"{int(cur_year.strftime('%Y')) - 1}-12-31"
        )
        for unit in unit_history_last_year:
            quantity_last_year += unit.quantity
        return quantity_last_year

    def dehydrate_quantity_current_year(self, history):
        quantity_current_year = 0
        id = getattr(history, "stock_model_id")
        cur_year = datetime.now()
        history = History.objects.all()
        unit_history_current_year = history.filter(
            stock_model_id=id,
            status='Расход',
            dateInstall__gte=f"{int(cur_year.strftime('%Y'))}-01-01",
            dateInstall__lte=f"{int(cur_year.strftime('%Y'))}-12-31"
        )
        for unit in unit_history_current_year:
            quantity_current_year += unit.quantity
        return quantity_current_year
