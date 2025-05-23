from dataclasses import dataclass
from datetime import datetime

from django.db.models import QuerySet
from import_export import fields, resources  # type: ignore[import-untyped]
from import_export.widgets import ForeignKeyWidget  # type: ignore[import-untyped]

from consumables.models import Accessories, Consumables
from device.models import Device
from stockroom.models.accessories import CategoryAcc, HistoryAcc, StockAcc
from stockroom.models.consumables import History, StockCat, Stockroom
from stockroom.models.devices import CategoryDev, StockDev


@dataclass
class BaseStockResource(resources.ModelResource):
    """_BaseStockResource_
    Resource defines how consumables | accessories form the stockroom are mapped to their export representations and handle exporting data.

    Other parameters:
            stock_model (type | None): _ForeignKey model for category field_
            stock_category (type | None): _ForeignKey model for manufacturer field_
    """

    stock_model: type | None = None
    stock_category: type | None = None

    name = fields.Field(
        column_name="Название",
        attribute="stock_model",
        widget=ForeignKeyWidget(stock_model, field="name"),
    )
    categories = fields.Field(
        column_name="Категория",
        attribute="categories",
        widget=ForeignKeyWidget(stock_category, field="name"),
    )
    manufacturer = fields.Field(
        column_name="Производитель",
        attribute="stock_model",
        widget=ForeignKeyWidget(stock_model, field="manufacturer__name"),
    )
    serial = fields.Field(
        column_name="Серийный номер",
        attribute="stock_model",
        widget=ForeignKeyWidget(stock_model, field="serial"),
    )
    serialImg = fields.Field(
        column_name="Фото серийного номера",
        attribute="stock_model",
        widget=ForeignKeyWidget(stock_model, field="serialImg"),
    )
    invent = fields.Field(
        column_name="Инвентарный номер",
        attribute="stock_model",
        widget=ForeignKeyWidget(stock_model, field="invent"),
    )
    inventImg = fields.Field(
        column_name="Фото инвентарного номера",
        attribute="stock_model",
        widget=ForeignKeyWidget(stock_model, field="inventImg"),
    )
    description = fields.Field(
        column_name="Описание",
        attribute="stock_model",
        widget=ForeignKeyWidget(stock_model, field="description"),
    )
    quantity = fields.Field(
        column_name="Количество",
        attribute="stock_model",
        widget=ForeignKeyWidget(stock_model, field="quantity"),
    )
    note = fields.Field(
        column_name="Примечание",
        attribute="stock_model",
        widget=ForeignKeyWidget(stock_model, field="note"),
    )
    dateAddToStock = fields.Field(
        column_name="Дата поступления на склад", attribute="dateAddToStock"
    )
    dateInstall = fields.Field(column_name="Дата установки", attribute="dateInstall")
    rack = fields.Field(column_name="Стеллаж", attribute="rack")
    shelf = fields.Field(column_name="Полка", attribute="shelf")


class StockDevResource(BaseStockResource):
    """_StockDevResource_
    Resource defines how devices from the stockroom are mapped to their export representations and handle exporting data.

    Other parameters:
            stock_model (type | None): _ForeignKey model for device category field_
            stock_category (type | None): _ForeignKey model for device manufacturer field_
    """

    stock_model = Device
    stock_category = CategoryDev

    hostname = fields.Field(
        column_name="Имя хоста",
        attribute="stock_model",
        widget=ForeignKeyWidget(stock_model, field="hostname"),
    )
    ip_address = fields.Field(
        column_name="IP адрес",
        attribute="stock_model",
        widget=ForeignKeyWidget(stock_model, field="ip_address"),
    )
    workplace = fields.Field(
        column_name="Рабочее место",
        attribute="stock_model",
        widget=ForeignKeyWidget(stock_model, field="workplace__name"),
    )

    class Meta:
        """_StockDevResource Meta_: _resource settings_"""

        model = StockDev
        exclude = ["stock_model"]


class StockConResource(BaseStockResource):
    """_StockConResource_
    Resource defines how consumables from the stockroom are mapped to their export representations and handle exporting data.

    Other parameters:
            stock_model (type | None): _ForeignKey model for consumable category field_
            stock_category (type | None): _ForeignKey model for consumable manufacturer field_
    """

    stock_model = Consumables
    stock_category = StockCat

    class Meta:
        """_StockConResource Meta_: _resource settings_"""

        model = Stockroom
        exclude = ["stock_model"]


class StockAccResource(BaseStockResource):
    """_StockAccResource_
    Resource defines how accessories from the stockroom are mapped to their export representations and handle exporting data.

    Other parameters:
            stock_model (type | None): _ForeignKey model for accessories category field_
            stock_category (type | None): _ForeignKey model for accessories manufacturer field_
    """

    stock_model = Accessories
    stock_category = CategoryAcc

    class Meta:
        """_StockAccResource Meta_: _resource settings_"""

        model = StockAcc
        exclude = ["stock_model"]


class ConsumableConsumptionResource(resources.ModelResource):
    """_ConsumableConsumptionResource_
    Resource defines how consumables are mapped to their export representations and handle exporting data.
    """

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
        column_name="Остаток",
        attribute="quantity",
    )
    require = fields.Field(
        column_name="Потребность",
    )

    def get_queryset(self):
        """_get_queryset_ Reterns queryset of the History model with distinct stock_model"""

        return self._meta.model.objects.order_by("stock_model").distinct("stock_model")

    class Meta:
        """_ConsumableConsumptionResource Meta_: _resource settings_"""

        model = History
        exclude = [
            "id",
            "stock_model_id",
            "device",
            "deviceId",
            "categories",
            "dateInstall",
            "user",
            "status",
            "note",
        ]

    @staticmethod
    def dehydrate_stock_model(history):
        """_dehydrate_stock_model_

        Args:
            history (Hystory):

        Returns:
            name (str): _name of stock_model_
        """
        name = getattr(history, "stock_model")
        return name

    @staticmethod
    def dehydrate_quantity(history):
        """_dehydrate_quantity_

        Args:
            history (Hystory):

        Returns:
            quantity (int): _quantity for the selected consumable._
        """

        id_ = getattr(history, "stock_model_id")
        consumables = Consumables.objects.all()
        if not consumables.filter(id=id_):
            quantity = 0
        else:
            quantity = consumables.filter(id=id_).get().quantity
        return quantity

    @staticmethod
    def dehydrate_devices(history):
        """_dehydrate_devices_

        Args:
            history (Hystory):

        Returns:
            devices (str): _name of all devices with the selected consumable._
        """

        id_ = getattr(history, "stock_model_id")
        device_list = []
        consumables = Consumables.objects.all()
        if not consumables.filter(id=id_):
            devices: int | str | QuerySet[Device, Device] = 0
        else:
            consumable = consumables.filter(id=id_).get()
            if not consumable.device.all():
                devices = ""
            else:
                devices = consumable.device.all().order_by("name").distinct("name")
                for device in devices:
                    device_list.append(device.name)
                devices = "|".join(device_list)
        return devices

    @staticmethod
    def dehydrate_devices_count(history):
        """_dehydrate_devices_count_

        Args:
            history (Hystory):

        Returns:
            devices_count (int): _quantity of all devices with the selected consumable._
        """

        id_ = getattr(history, "stock_model_id")
        consumables = Consumables.objects.all()
        if not consumables.filter(id=id_):
            devices_count = 0
        else:
            consumable = consumables.filter(id=id_).get()
            if not consumable.device.all():
                devices_count = 0
            else:
                devices_count = consumable.device.count()
        return devices_count

    @staticmethod
    def dehydrate_quantity_all(history):
        """_dehydrate_quantity_all_

        Args:
            history (Hystory):

        Returns:
            quantity_all (int): _quantity of all units of the selected consumable_
        """

        quantity_all = 0
        id_ = getattr(history, "stock_model_id")
        history = History.objects.all()
        unit_history_all = history.filter(
            stock_model_id=id_,
            status="Расход",
        )
        for unit in unit_history_all:
            quantity_all += unit.quantity
        return quantity_all

    @staticmethod
    def dehydrate_quantity_last_year(history):
        """_dehydrate_quantity_last_year_

        Args:
            history (Hystory):

        Returns:
            quantity_last_year (int): _quantity of all units of the selected consumable in the previous year_
        """

        quantity_last_year = 0
        id_ = getattr(history, "stock_model_id")
        cur_year = datetime.now()
        history = History.objects.all()
        unit_history_last_year = history.filter(
            stock_model_id=id_,
            status="Расход",
            dateInstall__gte=f"{int(cur_year.strftime('%Y')) - 1}-01-01",
            dateInstall__lte=f"{int(cur_year.strftime('%Y')) - 1}-12-31",
        )
        for unit in unit_history_last_year:
            quantity_last_year += unit.quantity
        return quantity_last_year

    @staticmethod
    def dehydrate_quantity_current_year(history):
        """_dehydrate_quantity_current_year_

        Args:
            history (Hystory):

        Returns:
            quantity_current_year (int): _quantity of all units of the selected consumable in the current year_
        """

        quantity_current_year = 0
        id_ = getattr(history, "stock_model_id")
        cur_year = datetime.now()
        history = History.objects.all()
        unit_history_current_year = history.filter(
            stock_model_id=id_,
            status="Расход",
            dateInstall__gte=f"{int(cur_year.strftime('%Y'))}-01-01",
            dateInstall__lte=f"{int(cur_year.strftime('%Y'))}-12-31",
        )
        for unit in unit_history_current_year:
            quantity_current_year += unit.quantity
        return quantity_current_year

    @staticmethod
    def dehydrate_require(history):
        """_dehydrate_require_

        Args:
            history (Hystory):

        Returns:
            require (int): _consumables need to be ordered_
        """

        QCY = int(
            ConsumableConsumptionResource.dehydrate_quantity_current_year(history)
        )
        QLY = int(ConsumableConsumptionResource.dehydrate_quantity_last_year(history))
        QS = int(ConsumableConsumptionResource.dehydrate_quantity(history))

        if QS <= 2 * QLY:
            requirement = abs(2 * QLY - QS + QCY)
        else:
            requirement = 0
        return requirement


class AccessoriesConsumptionResource(resources.ModelResource):
    """_AccessoriesConsumptionResource_
    Resource defines how accessories are mapped to their export representations and handle exporting data.
    """

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
        column_name="Остаток",
        attribute="quantity",
    )
    require = fields.Field(
        column_name="Потребность",
    )

    def get_queryset(self):
        """_get_queryset_ Reterns queryset of the HistoryAcc model with distinct stock_model names"""

        return (
            self._meta.model.objects.filter(status="Расход")
            .order_by("stock_model")
            .distinct("stock_model")
        )

    class Meta:
        """_AccessoriesConsumptionResource Meta_: _resource settings_"""

        model = HistoryAcc
        exclude = [
            "id",
            "stock_model_id",
            "device",
            "deviceId",
            "categories",
            "dateInstall",
            "user",
            "status",
            "note",
        ]

    @staticmethod
    def dehydrate_stock_model(historyacc):
        """_dehydrate_stock_model_

        Args:
            historyacc (HistoryAcc):

        Returns:
            name (str): _name of the stock_model_
        """

        name = getattr(historyacc, "stock_model")
        return name

    @staticmethod
    def dehydrate_quantity(historyacc):
        """_dehydrate_quantity_

        Args:
            historyacc (HistoryAcc):

        Returns:
            quantity (int): _quantity of the stock_model_
        """

        id_ = getattr(historyacc, "stock_model_id")
        consumables = Accessories.objects.all()
        if not consumables.filter(id=id_):
            quantity = 0
        else:
            quantity = consumables.filter(id=id_).get().quantity
        return quantity

    @staticmethod
    def dehydrate_devices(historyacc):
        """_dehydrate_devices_

        Args:
            historyacc (HistoryAcc):

        Returns:
            devices (str): _devices with the selected accessories._
        """

        id_ = getattr(historyacc, "stock_model_id")
        device_list = []
        consumables = Accessories.objects.all()
        if not consumables.filter(id=id_):
            devices: int | str | QuerySet[Device, Device] = 0
        else:
            consumable = consumables.filter(id=id_).get()
            if not consumable.device.all():
                devices = ""
            else:
                devices = consumable.device.all().order_by("name").distinct("name")
                for device in devices:
                    device_list.append(device.name)
                devices = "|".join(device_list)
        return devices

    @staticmethod
    def dehydrate_devices_count(historyacc):
        """_dehydrate_devices_count_

        Args:
            historyacc (HistoryAcc):

        Returns:
            devices_count (int): _number of devices with the selected accessories_
        """

        id_ = getattr(historyacc, "stock_model_id")
        consumables = Accessories.objects.all()
        if not consumables.filter(id=id_):
            devices_count = 0
        else:
            consumable = consumables.filter(id=id_).get()
            if not consumable.device.all():
                devices_count = 0
            else:
                devices_count = consumable.device.count()
        return devices_count

    @staticmethod
    def dehydrate_quantity_all(historyacc):
        """_dehydrate_quantity_all_

        Args:
            historyacc (HistoryAcc):

        Returns:
            quantity_all (int): _quantity of all units of the selected accessories in the current year_
        """

        quantity_all = 0
        id_ = getattr(historyacc, "stock_model_id")
        history = HistoryAcc.objects.all()
        unit_history_all = history.filter(
            stock_model_id=id_,
            status="Расход",
        )
        for unit in unit_history_all:
            quantity_all += unit.quantity
        return quantity_all

    @staticmethod
    def dehydrate_quantity_last_year(historyacc):
        """_dehydrate_quantity_last_year_

        Args:
            historyacc (HistoryAcc):

        Returns:
            quantity_last_year (int): _quantity of all units of the selected accessories in the previous year_
        """

        quantity_last_year = 0
        id_ = getattr(historyacc, "stock_model_id")
        cur_year = datetime.now()
        history = HistoryAcc.objects.all()
        unit_history_last_year = history.filter(
            stock_model_id=id_,
            status="Расход",
            dateInstall__gte=f"{int(cur_year.strftime('%Y')) - 1}-01-01",
            dateInstall__lte=f"{int(cur_year.strftime('%Y')) - 1}-12-31",
        )
        for unit in unit_history_last_year:
            quantity_last_year += unit.quantity
        return quantity_last_year

    @staticmethod
    def dehydrate_quantity_current_year(historyacc):
        """_dehydrate_quantity_current_year_

        Args:
            historyacc (HistoryAcc):

        Returns:
            quantity_current_year (int): _quantity of all units of the selected accessories in the current year_
        """

        quantity_current_year = 0
        id_ = getattr(historyacc, "stock_model_id")
        cur_year = datetime.now()
        history = HistoryAcc.objects.all()
        unit_history_current_year = history.filter(
            stock_model_id=id_,
            status="Расход",
            dateInstall__gte=f"{int(cur_year.strftime('%Y'))}-01-01",
            dateInstall__lte=f"{int(cur_year.strftime('%Y'))}-12-31",
        )
        for unit in unit_history_current_year:
            quantity_current_year += unit.quantity
        return quantity_current_year

    @staticmethod
    def dehydrate_require(historyacc):
        """_dehydrate_require_

        Args:
            historyacc (HistoryAcc):

        Returns:
            requirement (int): _requirement of the accessories_
        """

        QCY = int(
            AccessoriesConsumptionResource.dehydrate_quantity_current_year(historyacc)
        )
        QLY = int(
            AccessoriesConsumptionResource.dehydrate_quantity_last_year(historyacc)
        )
        QS = int(AccessoriesConsumptionResource.dehydrate_quantity(historyacc))

        if QS <= 2 * QLY:
            requirement = abs(2 * QLY - QS + QCY)
        else:
            requirement = 0
        return requirement
