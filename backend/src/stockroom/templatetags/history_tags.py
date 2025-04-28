from django import template

from stockroom.models.devices import HistoryDev

register = template.Library()


# device
@register.inclusion_tag("stock/history_dev_short_list.html")
def this_device_history(device_id):
    history_dev_list = HistoryDev.objects.filter(stock_model_id=device_id)

    return {
        "history_dev_list": history_dev_list,
        "table_head": "История использования устройства",
        "no_history": "Устройство не использовались",
    }


@register.inclusion_tag("stock/history_dev_short_list.html")
def dev_history_short():
    history_dev_list = HistoryDev.objects.all()[:5]

    return {
        "history_dev_list": history_dev_list,
        "table_head": "История использования устройств",
        "no_history": "Устройства не использовались",
    }


@register.inclusion_tag("stock/history_dev_short_list.html")
def device_decom_history():
    history_dev_list = HistoryDev.objects.filter(status="Списание")

    return {
        "history_dev_list": history_dev_list,
        "table_head": "История использования устройства",
        "no_history": "Устройство не использовались",
    }


@register.inclusion_tag("stock/history_dev_short_list.html")
def device_disp_history():
    history_dev_list = HistoryDev.objects.filter(status="Утилизация")

    return {
        "history_dev_list": history_dev_list,
        "table_head": "История использования устройства",
        "no_history": "Устройство не использовались",
    }
