from dataclasses import dataclass

from import_export import fields, resources  # type: ignore[import-untyped]
from import_export.widgets import ForeignKeyWidget  # type: ignore[import-untyped]

from consumables.models import AccCat, Accessories, Categories, Consumables
from counterparty.models import Manufacturer


@dataclass
class BaseResource(resources.ModelResource):
    """_BaseResource_
    Resource defines how consumables | accessories are mapped to their export representations and handle exporting data.

    Other parameters:
            category_model (type | None): _ForeignKey model for category field_
            manufacturer_model (type | None): _ForeignKey model for manufacturer field_
    """

    category_model: type | None = None
    manufacturer_model: type | None = None

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
    """_ConsumableResource_
    Resource defines how consumables are mapped to their export representations and handle exporting data.

    Other parameters:
            category_model (type | None): _ForeignKey model for category field_
            manufacturer_model (type | None): _ForeignKey model for manufacturer field_
    """

    category_model = Categories
    manufacturer_model = Manufacturer

    class Meta:
        """_ConsumableResource Meta_: _resource settings_"""

        model = Consumables
        exclude = ["id"]


class AccessoriesResource(BaseResource):
    """_AccessoriesResource_
    Resource defines how accessories are mapped to their export representations and handle exporting data.

    Other parameters:
            category_model (type | None): _ForeignKey model for category field_
            manufacturer_model (type | None): _ForeignKey model for manufacturer field_
    """

    category_model = AccCat
    manufacturer_model = Manufacturer

    class Meta:
        """_AccessoriesResource Meta_: _resource settings_"""

        model = Accessories
        exclude = ["id"]
