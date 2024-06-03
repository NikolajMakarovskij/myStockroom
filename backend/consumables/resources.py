from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from consumables.models import Consumables, Accessories, Categories, AccCat
from counterparty.models import Manufacturer
from dataclasses import dataclass


@dataclass
class BaseResource(resources.ModelResource):
    category_model: dict = None
    manufacturer_model: dict = None

    name = fields.Field(column_name="Название", attribute="name")
    categories = fields.Field(
        column_name="Категория",
        attribute="categories",
        widget=ForeignKeyWidget(category_model, field="name"),
    )
    manufacturer = fields.Field(
        column_name="Производитель",
        attribute="manufacturer",
        widget=ForeignKeyWidget(manufacturer_model, field="name"),
    )
    serial = fields.Field(column_name="Серийный номер", attribute="serial")
    serialImg = fields.Field(column_name="Фото серийного номера", attribute="serialImg")
    invent = fields.Field(column_name="Инвентарный номер", attribute="invent")
    inventImg = fields.Field(
        column_name="Фото инвентарного номера", attribute="inventImg"
    )
    description = fields.Field(column_name="Описание", attribute="description")
    quantity = fields.Field(column_name="Количество", attribute="quantity")
    note = fields.Field(column_name="Примечание", attribute="note")


class ConsumableResource(BaseResource):
    category_model = Categories
    manufacturer_model = Manufacturer

    class Meta:
        model = Consumables
        exclude = ["id"]


class AccessoriesResource(BaseResource):
    category_model = AccCat
    manufacturer_model = Manufacturer

    class Meta:
        model = Accessories
        exclude = ["id"]
