from django.conf import settings
from django.contrib.auth.models import User


def create_session(client):
    """Creates a user and a session"""
    User.objects.create_superuser("admin", "foo@foo.com", "admin")
    client.login(username="admin", password="admin")
    session = client.session
    session[settings.STOCK_SESSION_ID] = "6fk7mglhnq7f3avej9rmlshjyrokal3l"
    session.save()
    return client


def create_consumable() -> dict:
    """Service function. Creates a category and a stock_model"""
    from consumables.models import Categories, Consumables

    if Consumables.objects.filter(name="my_consumable").aexists():
        Categories.objects.create(name="my_category", slug="my_category")
        Consumables.objects.create(
            name="my_consumable", categories=Categories.objects.get(name="my_category")
        )
        get_consumable = Consumables.objects.get(name="my_consumable")
    else:
        get_consumable = Consumables.objects.get(name="my_consumable")
    return get_consumable


def create_accessories() -> dict:
    """Service function. Creates a category and stock_model"""
    from consumables.models import AccCat, Accessories

    if Accessories.objects.filter(name="my_consumable").aexists():
        AccCat.objects.create(name="my_category", slug="my_category")
        Accessories.objects.create(
            name="my_consumable", categories=AccCat.objects.get(name="my_category")
        )
        get_accessories = Accessories.objects.get(name="my_consumable")
    else:
        get_accessories = Accessories.objects.get(name="my_consumable")
    return get_accessories


def create_devices() -> dict:
    """Service function. Creates a category and stock_model"""
    from device.models import Device, DeviceCat

    if Device.objects.filter(name="my_consumable").aexists():
        DeviceCat.objects.create(name="my_category", slug="my_category")
        Device.objects.create(
            name="my_consumable", categories=DeviceCat.objects.get(name="my_category")
        )
        get_device = Device.objects.get(name="my_consumable")
    else:
        get_device = Device.objects.get(name="my_consumable")
    return get_device


def add_consumables_in_devices(consumable: dict, accessories: dict) -> dict:
    """Service function. Creates a category, stock_model and stock_model. Return stock_model"""
    from device.models import Device

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
            device.consumable.set([consumable.id])
    if not accessories:
        pass
    else:
        for device in Device.objects.all():
            device.accessories.set([accessories.id])
    get_devices = Device.objects.all()
    return get_devices
