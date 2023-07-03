from django import template

from ..models import History, HistoryAcc, HistoryDev
from device.models import Device, Device_cat

register = template.Library()



@register.inclusion_tag('stock/device_move_history_list.html')
def this_device_history(device_id):
    device_move_list = HistoryDev.objects.filter(deviciesId=device_id)

    return {"device_move_list":device_move_list}

@register.inclusion_tag('stock/device_con_history_list.html')
def this_device_con_history(device_id):
    device_con_history_list = History.objects.filter(deviceId=device_id)

    return {"device_con_history_list":device_con_history_list}

@register.inclusion_tag('stock/device_acc_history_list.html')
def this_device_acc_history(device_id):
    device_acc_history_list = HistoryAcc.objects.filter(deviceId=device_id)

    return {"device_acc_history_list":device_acc_history_list}



