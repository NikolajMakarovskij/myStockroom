from rest_framework import serializers

from ..stock.stock import AccStock, ConStock, DevStock


class AddToStockSerializer(serializers.Serializer[ConStock | AccStock | DevStock]):
    """_AddToStockSerializer_ Serializes data in the form for adding an Consumables | Accessories | Device item to the stockroom

    Other parameters:
        model_id (UUID): _id of Consumables | Accessories | Device item_
        quantity (int): _quantity of Consumables | Accessories | Device item to be added to the stockroom_
        number_rack (int): _rack number in the stockroom where item will be placed_
        number_shelf (int): _shelf number in the stockroom where item will be placed_
        username (str): _username of the person adding item to the stockroom_
    """

    model_id = serializers.UUIDField(required=True)
    quantity = serializers.IntegerField(required=True)
    number_rack = serializers.IntegerField(required=True)
    number_shelf = serializers.IntegerField(required=True)
    username = serializers.CharField(required=True)


class AddToDeviceSerializer(serializers.Serializer[ConStock | AccStock]):
    """_AddToDeviceSerializer_ Serializes data in the form for adding an Consumables | Accessories item to the device

    Other parameters:
        model_id (UUID): _id of Consumables | Accessories item_
        device (UUID): _id of the device to which Consumables | Accessories item will be added_
        quantity (int): _quantity of Consumables | Accessories item to be added to the device_
        note (str): _additional information about the addition of Consumables | Accessories item to the device_
        username (str): _username of the person adding Consumables | Accessories item to the device_
    """

    model_id = serializers.UUIDField(required=True)
    device = serializers.UUIDField(required=True)
    quantity = serializers.IntegerField(required=True)
    note = serializers.CharField(required=False)
    username = serializers.CharField(required=True)


class RemoveFromStockSerializer(serializers.Serializer[ConStock | AccStock | DevStock]):
    """_RemoveFromStockSerializer_ Serializes data in the form for removing an Consumables | Accessories | Device item from the stockroom

    Other parameters:
        model_id (UUID): _id of Consumables | Accessories | Device item_
        username (str): _username of the person removing item from the stockroom_
    """

    model_id = serializers.UUIDField(required=True)
    username = serializers.CharField(required=True)


class MoveDeviceSerializer(serializers.Serializer[DevStock]):
    """_MoveDeviceSerializer_ Serializes data in the form for moving a Device item from the stockroom | Workplace to the workplace

    Other parameters:
        model_id (UUID): _id of Device item_
        workplace_id (UUID): _id of the workplace to which Device item will be moved_
        note (str): _additional information about the movement of Device item from the stockroom to the workplace_
        username (str): _username of the person moving Device item from the stockroom to the workplace_
    """

    model_id = serializers.UUIDField(required=True)
    workplace_id = serializers.UUIDField(required=True)
    note = serializers.CharField(required=False)
    username = serializers.CharField(required=True)


class AddHistoryDeviceSerializer(serializers.Serializer[DevStock]):
    """_AddHistoryDeviceSerializer_ Serializes data in the form for adding a history of a Device item

    Other parameters:
        model_id (UUID): _id of Device item_
        status_choice (str): _status of the Device item_
        note (str): _additional information about the status of the Device item_
        username (str): _username of the person adding a history of the Device item_
    """

    model_id = serializers.UUIDField(required=True)
    status_choice = serializers.CharField(required=True)
    note = serializers.CharField(required=False)
    username = serializers.CharField(required=True)
