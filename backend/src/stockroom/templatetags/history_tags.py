from datetime import datetime

from django import template

from consumables.models import Accessories, Consumables
from stockroom.models.accessories import HistoryAcc
from stockroom.models.consumables import History
from stockroom.models.devices import HistoryDev
from device.models import Device
from django.db.models import QuerySet

register = template.Library()


# device
@register.inclusion_tag("stock/history_dev_short_list.html")
def this_device_history(device_id):
    """_this_device_history_
    returns all entries from the history for the current device

    Args:
        device_id (UUID): _description_

    Returns:
        history_dev_list (HistoryDev): _the list of entries for the Devcie instance_
        table_head (str): _name of the table_
        no_history (str): _if there are no records_
    """
    history_dev_list = HistoryDev.objects.filter(stock_model_id=device_id)

    return {
        "history_dev_list": history_dev_list,
        "table_head": "История использования устройства",
        "no_history": "Устройство не использовались",
    }


@register.inclusion_tag("stock/history_dev_short_list.html")
def dev_history_short():
    """_dev_history_short_
    returns first five entries from the history for the current device

    Returns:
        history_dev_list (HistoryDev): _the list of entries for the Devcie history instance_
        table_head (str): _name of the table_
        no_history (str): _if there are no records_
    """
    history_dev_list = HistoryDev.objects.all()[:5]

    return {
        "history_dev_list": history_dev_list,
        "table_head": "История использования устройств",
        "no_history": "Устройства не использовались",
    }


@register.inclusion_tag("stock/history_dev_short_list.html")
def device_decom_history():
    """_device_decom_history_
    returns all entries from the history for the current device with status "Списание"

    Returns:
        history_dev_list (HistoryDev): _the list of entries for the Devcie Devcie history instance_
        table_head (str): _name of the table_
        no_history (str): _if there are no records_
    """
    history_dev_list = HistoryDev.objects.filter(status="Списание")

    return {
        "history_dev_list": history_dev_list,
        "table_head": "История использования устройства",
        "no_history": "Устройство не использовались",
    }


@register.inclusion_tag("stock/history_dev_short_list.html")
def device_disp_history():
    """_device_disp_history_
    returns all entries from the history for the current device with status "Утилизация"

    Returns:
        history_dev_list (HistoryDev): _the list of entries for the Devcie history instance_
        table_head (str): _name of the table_
        no_history (str): _if there are no records_
    """
    history_dev_list = HistoryDev.objects.filter(status="Утилизация")

    return {
        "history_dev_list": history_dev_list,
        "table_head": "История использования устройства",
        "no_history": "Устройство не использовались",
    }


# consumables
@register.inclusion_tag("stock/history_short_list.html")
def this_device_con_history(device_id):
    """_this_device_con_history_
    returns all entries from the history consumables for the current device

    Args:
        device_id (UUID): _description_

    Returns:
        history_list (History): _the list of entries for the Devcie instance_
        table_head (str): _name of the table_
        no_history (str): _if there are no records_
    """
    history_list = History.objects.filter(deviceId=device_id)

    return {
        "history_list": history_list,
        "table_head": "История использования расходников",
        "no_history": "Расходники не использовались",
    }


@register.inclusion_tag("stock/history_short_list.html")
def this_con_history(consumable_id):
    """_this_con_history_
    returns all entries from the history for the current consumable

    Args:
        consumable_id (UUID): _description_

    Returns:
        history_list (History): _the list of entries for the Consumables instance_
        table_head (str): _name of the table_
        no_history (str): _if there are no records_
    """
    history_list = History.objects.filter(stock_model_id=consumable_id)

    return {
        "history_list": history_list,
        "table_head": "История использования расходника",
        "no_history": "Расходники не использовались",
    }


@register.inclusion_tag("stock/consumption_list.html")
def consumption(consumable_id):
    """_consumption_
    returns a list of consumable supplies for each device

    Args:
        consumable_id (UUID): _description_

    Returns:
        device_name (str): _name of Device instance_,
        device_count (int): _device count_,
        quantity_all (int): _the amount spent over the entire time_,
        quantity_last_year (int): _the amount spent in the previous year_,
        quantity_current_year (int): _the amount spent in the current year_,
        quantity (int): _stock balance_,
        requirement (int): _the need for the next year_,
    """
    cur_year = datetime.now()
    history = History.objects.all()
    consumables = Consumables.objects.all()
    device_count = 0
    device_name: QuerySet[Device, Device] | str = ""
    quantity = 0
    if not consumables.filter(id=consumable_id):
        pass
    else:
        consumable = consumables.filter(id=consumable_id).get()
        quantity = consumable.quantity
        if not consumable.device.all():
            pass
        else:
            device_name = consumable.device.all().order_by("name").distinct("name") #
            device_count = consumable.device.count()

    unit_history_all = history.filter(
        stock_model_id=consumable_id,
        status="Расход",
    )
    unit_history_last_year = history.filter(
        stock_model_id=consumable_id,
        status="Расход",
        dateInstall__gte=f"{int(cur_year.strftime('%Y'))-1}-01-01",
        dateInstall__lte=f"{int(cur_year.strftime('%Y'))-1}-12-31",
    )
    unit_history_current_year = history.filter(
        stock_model_id=consumable_id,
        status="Расход",
        dateInstall__gte=f"{cur_year.strftime('%Y')}-01-01",
        dateInstall__lte=f"{cur_year.strftime('%Y')}-12-31",
    )
    quantity_all = 0
    quantity_last_year = 0
    quantity_current_year = 0
    for unit in unit_history_all:
        quantity_all += unit.quantity
    for unit in unit_history_last_year:
        quantity_last_year += unit.quantity
    for unit in unit_history_current_year:
        quantity_current_year += unit.quantity
    if quantity <= 2 * quantity_last_year:
        requirement = abs(2 * quantity_last_year - quantity + quantity_current_year)
    else:
        requirement = 0
    return {
        "device_name": device_name,
        "device_count": device_count,
        "quantity_all": quantity_all,
        "quantity_last_year": quantity_last_year,
        "quantity_current_year": quantity_current_year,
        "quantity": quantity,
        "requirement": requirement,
    }


@register.inclusion_tag("stock/history_short_list.html")
def consumables_history():
    """_consumables_history_
    returns first five entries from the history for the current consumable

    Returns:
        history_list (History): _the list of entries for the Consumable history instance_
        table_head (str): _name of the table_
        no_history (str): _if there are no records_
    """
    history_list = History.objects.all()[:5]

    return {
        "history_list": history_list,
        "table_head": "История расходников",
        "no_history": "Расходники не использовались",
    }


# accessories
@register.inclusion_tag("stock/history_acc_short_list.html")
def this_device_acc_history(device_id):
    """_this_device_acc_history_
    returns all entries from the history accessories for the current device

    Args:
        device_id (UUID): _description_

    Returns:
        history_list (HistoryAcc): _the list of entries for the Device history instance_
        table_head (str): _name of the table_
        no_history (str): _if there are no records_
    """
    history_list = HistoryAcc.objects.filter(deviceId=device_id)

    return {
        "history_acc_list": history_list,
        "table_head": "История использования комплектующих",
        "no_history": "Комплектующие не использовались",
    }


@register.inclusion_tag("stock/history_acc_short_list.html")
def this_acc_history(accessories_id):
    """_this_acc_history_
    returns all entries from the history accessories for the current accessory
    Args:
        accessories_id (UUID): _description_

    Returns:
        history_list (HistoryAcc): _the list of entries for the Accessories history instance_
        table_head (str): _name of the table_
        no_history (str): _if there are no records_
    """

    history_list = HistoryAcc.objects.filter(stock_model_id=accessories_id)

    return {
        "history_acc_list": history_list,
        "table_head": "История использования комплектующего",
        "no_history": "Комплектующее не использовалось",
    }


@register.inclusion_tag("stock/history_acc_short_list.html")
def accessories_history():
    """_accessories_history_
    returns first five entries from the history for the current accessory

    Returns:
        history_list (HistoryAcc): _the list of entries for the Accessories history instance_
        table_head (str): _name of the table_
        no_history (str): _if there are no records_
    """

    history_list = HistoryAcc.objects.all()[:5]

    return {
        "history_acc_list": history_list,
        "table_head": "История комплектующих",
        "no_history": "Комплектующее не использовались",
    }


@register.inclusion_tag("stock/consumption_list.html")
def consumption_acc(consumable_id):
    """_consumption_acc_
    returns accessories consumption data

    Args:
        consumable_id (UUID): _description_

    Returns:
        device_name (str): _name of the device_
        device_count (int): _count of the device_
        quantity_all (int): _total quantity_
        quantity_last_year (int): _quantity for the last year_
        quantity_current_year (int): _quantity for the current year_
        quantity (int): _stock balance_
        requirement (int): _the need for the next year_
    """

    cur_year = datetime.now()
    history = HistoryAcc.objects.all()
    consumables = Accessories.objects.all()
    device_count = 0
    device_name: QuerySet[Device, Device] | str = ""
    quantity = 0
    if not consumables.filter(id=consumable_id):
        pass
    else:
        consumable = consumables.filter(id=consumable_id).get()
        quantity = consumable.quantity
        if not consumable.device.all():
            pass
        else:
            device_name = consumable.device.all().order_by("name").distinct("name")
            device_count = consumable.device.count()
    unit_history_all = history.filter(
        stock_model_id=consumable_id,
        status="Расход",
    )
    unit_history_last_year = history.filter(
        stock_model_id=consumable_id,
        status="Расход",
        dateInstall__gte=f"{int(cur_year.strftime('%Y'))-1}-01-01",
        dateInstall__lte=f"{int(cur_year.strftime('%Y'))-1}-12-31",
    )
    unit_history_current_year = history.filter(
        stock_model_id=consumable_id,
        status="Расход",
        dateInstall__gte=f"{cur_year.strftime('%Y')}-01-01",
        dateInstall__lte=f"{cur_year.strftime('%Y')}-12-31",
    )
    quantity_all = 0
    quantity_last_year = 0
    quantity_current_year = 0
    for unit in unit_history_all:
        quantity_all += unit.quantity
    for unit in unit_history_last_year:
        quantity_last_year += unit.quantity
    for unit in unit_history_current_year:
        quantity_current_year += unit.quantity
    if quantity <= 2 * quantity_last_year:
        requirement = abs(2 * quantity_last_year - quantity + quantity_current_year)
    else:
        requirement = 0
    return {
        "device_name": device_name,
        "device_count": device_count,
        "quantity_all": quantity_all,
        "quantity_last_year": quantity_last_year,
        "quantity_current_year": quantity_current_year,
        "quantity": quantity,
        "requirement": requirement,
    }
