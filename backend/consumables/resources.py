from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget

from consumables.models import Consumables, Accessories, Categories, AccCat
from counterparty.models import Manufacturer


class ConsumableResource(resources.ModelResource):
    name = fields.Field(
        column_name='Название',
        attribute='name'
    )
    categories = fields.Field(
        column_name='Категория',
        attribute='categories',
        widget=ForeignKeyWidget(Categories, field='name')
    )
    manufacturer = fields.Field(
        column_name='Производитель',
        attribute='manufacturer',
        widget=ForeignKeyWidget(Manufacturer, field='name')
    )
    serial = fields.Field(
        column_name='Серийный номер',
        attribute='serial'
    )
    serialImg = fields.Field(
        column_name='Фото серийного номера',
        attribute='serialImg'
    )
    invent = fields.Field(
        column_name='Инвентарный номер',
        attribute='invent'
    )
    inventImg = fields.Field(
        column_name='Фото инвентарного номера',
        attribute='inventImg'
    )
    description = fields.Field(
        column_name='Описание',
        attribute='description'
    )
    quantity = fields.Field(
        column_name='Количество',
        attribute='quantity'
    )
    note = fields.Field(
        column_name='Примечание',
        attribute='note'
    )

    class Meta:
        model = Consumables


class AccessoriesResource(resources.ModelResource):
    name = fields.Field(
        column_name='Название',
        attribute='name'
    )
    categories = fields.Field(
        column_name='Категория',
        attribute='categories',
        widget=ForeignKeyWidget(AccCat, field='name')
    )
    manufacturer = fields.Field(
        column_name='Производитель',
        attribute='manufacturer',
        widget=ForeignKeyWidget(Manufacturer, field='name')
    )
    serial = fields.Field(
        column_name='Серийный номер',
        attribute='serial'
    )
    serialImg = fields.Field(
        column_name='Фото серийного номера',
        attribute='serialImg'
    )
    invent = fields.Field(
        column_name='Инвентарный номер',
        attribute='invent'
    )
    inventImg = fields.Field(
        column_name='Фото инвентарного номера',
        attribute='inventImg'
    )
    description = fields.Field(
        column_name='Описание',
        attribute='description'
    )
    quantity = fields.Field(
        column_name='Количество',
        attribute='quantity'
    )
    note = fields.Field(
        column_name='Примечание',
        attribute='note'
    )

    class Meta:
        model = Accessories
