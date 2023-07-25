from django import template
from ..models import History, HistoryAcc, HistoryDev

register = template.Library()


# device
@register.inclusion_tag('stock/history_dev_short_list.html')
def this_device_history(device_id):
    history_dev_list = HistoryDev.objects.filter(stock_model_id=device_id)

    return {
        "history_dev_list": history_dev_list,
        "table_head": "История использования устройства",
        "no_history": "Устройство не использовались"
        }


@register.inclusion_tag('stock/history_dev_short_list.html')
def dev_history_short():
    history_dev_list = HistoryDev.objects.all()[:5]

    return {
        "history_dev_list": history_dev_list,
        "table_head": "История использования устройств",
        "no_history": "Устройства не использовались"}


@register.inclusion_tag('stock/history_dev_short_list.html')
def device_decom_history():
    history_dev_list = HistoryDev.objects.filter(status="Списание")

    return {
        "history_dev_list": history_dev_list,
        "table_head": "История использования устройства",
        "no_history": "Устройство не использовались"
        }


@register.inclusion_tag('stock/history_dev_short_list.html')
def device_disp_history():
    history_dev_list = HistoryDev.objects.filter(status="Утилизация")

    return {
        "history_dev_list": history_dev_list,
        "table_head": "История использования устройства",
        "no_history": "Устройство не использовались"
        }


# consumables
@register.inclusion_tag('stock/history_short_list.html')
def this_device_con_history(device_id):
    history_list = History.objects.filter(stock_model_id=device_id)

    return {
        "history_list": history_list,
        "table_head": "История использования расходников",
        "no_history": "Расходники не использовались"
        }


@register.inclusion_tag('stock/history_short_list.html')
def this_con_history(consumable_id):
    history_list = History.objects.filter(stock_model_id=consumable_id)

    return {
        "history_list": history_list,
        "table_head": "История использования расходника",
        "no_history": "Расходники не использовались"
        }


@register.inclusion_tag('stock/history_short_list.html')
def consumables_history():
    history_list = History.objects.all()[:5]

    return {
        "history_list": history_list,
        "table_head": "История расходников",
        "no_history": "Расходники не использовались"
        }


# accessories
@register.inclusion_tag('stock/history_acc_short_list.html')
def this_device_acc_history(device_id):
    history_list = HistoryAcc.objects.filter(stock_model_id=device_id)

    return {
        "history_acc_list": history_list,
        "table_head": "История использования комплектующих",
        "no_history": "Комплектующие не использовались"
        }


@register.inclusion_tag('stock/history_acc_short_list.html')
def this_acc_history(accessories_id):
    history_list = HistoryAcc.objects.filter(stock_model_id=accessories_id)

    return {
        "history_acc_list": history_list,
        "table_head": "История использования комплектующего",
        "no_history": "Комплектующее не использовалось"
        }


@register.inclusion_tag('stock/history_acc_short_list.html')
def accessories_history():
    history_list = HistoryAcc.objects.all()[:5]

    return {
        "history_acc_list": history_list,
        "table_head": "История комплектующих",
        "no_history": "Комплектующее не использовались"
        }
