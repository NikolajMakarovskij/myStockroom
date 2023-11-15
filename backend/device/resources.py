from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget

from consumables.models import Consumables, Accessories
from counterparty.models import Manufacturer
from device.models import Device, DeviceCat
from workplace.models import Workplace


class DeviceResource(resources.ModelResource):
    name = fields.Field(
        column_name='Название',
        attribute='name',
    )
    hostname = fields.Field(
        column_name='Имя хоста',
        attribute='hostname',
    )
    ip_address = fields.Field(
        column_name='IP адрес',
        attribute='ip_address',
    )
    login = fields.Field(
        column_name='Логин',
        attribute='login',
    )
    pwd = fields.Field(
        column_name='Пароль',
        attribute='pwd',
    )
    categories = fields.Field(
        column_name='Категория',
        attribute='categories',
        widget=ForeignKeyWidget(DeviceCat, field='name')
    )
    manufacturer = fields.Field(
        column_name='Производитель',
        attribute='manufacturer',
        widget=ForeignKeyWidget(Manufacturer, field='name')
    )
    serial = fields.Field(
        column_name='Серийный номер',
        attribute='serial',
    )
    serialImg = fields.Field(
        column_name='Фото серийного номера',
        attribute='serialImg',
    )
    invent = fields.Field(
        column_name='Инвентарный номер',
        attribute='invent',
    )
    inventImg = fields.Field(
        column_name='Фото инвентарного номера',
        attribute='inventImg',
    )
    description = fields.Field(
        column_name='Описание',
        attribute='description',
    )
    workplace = fields.Field(
        column_name='Рабочее место',
        attribute='workplace',
        widget=ForeignKeyWidget(Workplace, field='name')
    )
    consumable = fields.Field(
        column_name='Расходник',
        attribute='consumable',
        widget=ManyToManyWidget(Consumables, field='name', separator='|')
    )
    accessories = fields.Field(
        column_name='Комплектующее',
        attribute='accessories',
        widget=ManyToManyWidget(Accessories, field='name', separator='|')
    )
    quantity = fields.Field(
        column_name='Количество',
        attribute='quantity',
    )
    note = fields.Field(
        column_name='Примечание',
        attribute='note',
    )

    class Meta:
        model = Device
