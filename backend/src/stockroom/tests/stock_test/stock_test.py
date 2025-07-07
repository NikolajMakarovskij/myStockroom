from django.db.models import Model
from django.db.models.query import QuerySet

from consumables.models import AccCat, Accessories, Categories, Consumables
from device.models import Device, DeviceCat


def create_consumable() -> Model:
    """Service function. Creates a category and a stock_model"""

    if Consumables.objects.filter(name="my_consumable").aexists():
        Categories.objects.create(name="my_category", slug="my_category")
        Consumables.objects.create(
            name="my_consumable", categories=Categories.objects.get(name="my_category")
        )
        get_consumable = Consumables.objects.get(name="my_consumable")
    else:
        get_consumable = Consumables.objects.get(name="my_consumable")
    return get_consumable


def create_accessories() -> Model:
    """Service function. Creates a category and stock_model"""

    if Accessories.objects.filter(name="my_consumable").aexists():
        AccCat.objects.create(name="my_category", slug="my_category")
        Accessories.objects.create(
            name="my_consumable", categories=AccCat.objects.get(name="my_category")
        )
        get_accessories = Accessories.objects.get(name="my_consumable")
    else:
        get_accessories = Accessories.objects.get(name="my_consumable")
    return get_accessories


def create_devices() -> Model:
    """Service function. Creates a category and stock_model"""

    if Device.objects.filter(name="my_consumable").aexists():
        DeviceCat.objects.create(name="my_category", slug="my_category")
        Device.objects.create(
            name="my_consumable", categories=DeviceCat.objects.get(name="my_category")
        )
        get_device = Device.objects.get(name="my_consumable")
    else:
        get_device = Device.objects.get(name="my_consumable")
    return get_device


def add_consumables_in_devices(
    consumable: Model | None, accessories: Model | None
) -> QuerySet[Device, Device]:
    """Service function. Creates a category, stock_model and stock_model. Return stock_model"""

    Device.objects.bulk_create(
        [
            Device(name="device 1"),
            Device(name="device 2"),
            Device(name="device 3"),
        ]
    )
    if not consumable:
        pass
    else:
        for device in Device.objects.all():
            device.consumable.set([consumable.id])  # type: ignore[attr-defined]
    if not accessories:
        pass
    else:
        for device in Device.objects.all():
            device.accessories.set([accessories.id])  # type: ignore[attr-defined]
    get_devices = Device.objects.all()
    return get_devices
