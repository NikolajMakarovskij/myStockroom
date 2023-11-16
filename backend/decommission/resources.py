from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget

from decommission.models import Decommission, Disposal, CategoryDec, CategoryDis
from device.models import Device


class DecommissionResource(resources.ModelResource):

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
        widget=ForeignKeyWidget(CategoryDec, field='name')
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
    date = fields.Field(
        column_name='Дата',
        attribute='date'
    )

    class Meta:
        model = Decommission


class DisposalResource(resources.ModelResource):

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
        widget=ForeignKeyWidget(CategoryDis, field='name')
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
    date = fields.Field(
        column_name='Дата',
        attribute='date'
    )

    class Meta:
        model = Disposal