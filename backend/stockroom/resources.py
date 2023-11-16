from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget

from device.models import Device
from consumables.models import Consumables, Accessories
from stockroom.models.devices import StockDev, CategoryDev
from stockroom.models.consumables import Stockroom, StockCat, History
from stockroom.models.accessories import StockAcc, CategoryAcc, HistoryAcc

from datetime import datetime


class StockDevResource(resources.ModelResource):
    name = fields.Field(
        column_name='Название',
        attribute='stock_model',
        widget=ForeignKeyWidget(Device, field='name')
    )
    hostname = fields.Field(
        column_name='Имя хоста',
        attribute='stock_model',
        widget=ForeignKeyWidget(Device, field='hostname')
    )
    ip_address = fields.Field(
        column_name='IP адрес',
        attribute='stock_model',
        widget=ForeignKeyWidget(Device, field='ip_address')
    )
    categories = fields.Field(
        column_name='Категория',
        attribute='categories',
        widget=ForeignKeyWidget(CategoryDev, field='name')
    )
    manufacturer = fields.Field(
        column_name='Производитель',
        attribute='stock_model',
        widget=ForeignKeyWidget(Device, field='manufacturer__name')
    )
    serial = fields.Field(
        column_name='Серийный номер',
        attribute='stock_model',
        widget=ForeignKeyWidget(Device, field='serial')
    )
    serialImg = fields.Field(
        column_name='Фото серийного номера',
        attribute='stock_model',
        widget=ForeignKeyWidget(Device, field='serialImg')
    )
    invent = fields.Field(
        column_name='Инвентарный номер',
        attribute='stock_model',
        widget=ForeignKeyWidget(Device, field='invent')
    )
    inventImg = fields.Field(
        column_name='Фото инвентарного номера',
        attribute='stock_model',
        widget=ForeignKeyWidget(Device, field='inventImg')
    )
    description = fields.Field(
        column_name='Описание',
        attribute='stock_model',
        widget=ForeignKeyWidget(Device, field='description')
    )
    workplace = fields.Field(
        column_name='Рабочее место',
        attribute='stock_model',
        widget=ForeignKeyWidget(Device, field='workplace__name')
    )
    quantity = fields.Field(
        column_name='Количество',
        attribute='stock_model',
        widget=ForeignKeyWidget(Device, field='quantity')
    )
    note = fields.Field(
        column_name='Примечание',
        attribute='stock_model',
        widget=ForeignKeyWidget(Device, field='note')
    )
    dateAddToStock = fields.Field(
        column_name='Дата постановки',
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

    class Meta:
        model = StockDev


class StockConResource(resources.ModelResource):
    name = fields.Field(
        column_name='Название',
        attribute='stock_model',
        widget=ForeignKeyWidget(Consumables, field='name')
    )
    categories = fields.Field(
        column_name='Категория',
        attribute='categories',
        widget=ForeignKeyWidget(StockCat, field='name')
    )
    manufacturer = fields.Field(
        column_name='Производитель',
        attribute='stock_model',
        widget=ForeignKeyWidget(Consumables, field='manufacturer__name')
    )
    serial = fields.Field(
        column_name='Серийный номер',
        attribute='stock_model',
        widget=ForeignKeyWidget(Consumables, field='serial')
    )
    serialImg = fields.Field(
        column_name='Фото серийного номера',
        attribute='stock_model',
        widget=ForeignKeyWidget(Consumables, field='serialImg')
    )
    invent = fields.Field(
        column_name='Инвентарный номер',
        attribute='stock_model',
        widget=ForeignKeyWidget(Consumables, field='invent')
    )
    inventImg = fields.Field(
        column_name='Фото инвентарного номера',
        attribute='stock_model',
        widget=ForeignKeyWidget(Consumables, field='inventImg')
    )
    description = fields.Field(
        column_name='Описание',
        attribute='stock_model',
        widget=ForeignKeyWidget(Consumables, field='description')
    )
    quantity = fields.Field(
        column_name='Количество',
        attribute='stock_model',
        widget=ForeignKeyWidget(Consumables, field='quantity')
    )
    note = fields.Field(
        column_name='Примечание',
        attribute='stock_model',
        widget=ForeignKeyWidget(Consumables, field='note')
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

    class Meta:
        model = Stockroom


class StockAccResource(resources.ModelResource):
    name = fields.Field(
        column_name='Название',
        attribute='stock_model',
        widget=ForeignKeyWidget(Accessories, field='name')
    )
    categories = fields.Field(
        column_name='Категория',
        attribute='categories',
        widget=ForeignKeyWidget(CategoryAcc, field='name')
    )
    manufacturer = fields.Field(
        column_name='Производитель',
        attribute='stock_model',
        widget=ForeignKeyWidget(Accessories, field='manufacturer__name')
    )
    serial = fields.Field(
        column_name='Серийный номер',
        attribute='stock_model',
        widget=ForeignKeyWidget(Accessories, field='serial')
    )
    serialImg = fields.Field(
        column_name='Фото серийного номера',
        attribute='stock_model',
        widget=ForeignKeyWidget(Accessories, field='serialImg')
    )
    invent = fields.Field(
        column_name='Инвентарный номер',
        attribute='stock_model',
        widget=ForeignKeyWidget(Accessories, field='invent')
    )
    inventImg = fields.Field(
        column_name='Фото инвентарного номера',
        attribute='stock_model',
        widget=ForeignKeyWidget(Accessories, field='inventImg')
    )
    description = fields.Field(
        column_name='Описание',
        attribute='stock_model',
        widget=ForeignKeyWidget(Accessories, field='description')
    )
    quantity = fields.Field(
        column_name='Количество',
        attribute='stock_model',
        widget=ForeignKeyWidget(Accessories, field='quantity')
    )
    note = fields.Field(
        column_name='Примечание',
        attribute='stock_model',
        widget=ForeignKeyWidget(Accessories, field='note')
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

    class Meta:
        model = StockAcc


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
        exclude = ['id', 'stock_model_id', 'device', 'deviceId', 'categories', 'dateInstall', 'user', 'status',	'note']

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
            dateInstall__gte=f"{int(cur_year.strftime('%Y'))-1}-01-01",
            dateInstall__lte=f"{int(cur_year.strftime('%Y'))-1}-12-31"
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


