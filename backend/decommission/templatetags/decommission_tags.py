from django import template
from ..models import HistoryDis, HistoryDec

register = template.Library()


# Decommission
@register.inclusion_tag('decom/history_decom_short_list.html')
def decom_history_short():
    history_dev_list = HistoryDec.objects.all()[:5]

    return {
        "history_list": history_dev_list,
        "table_head": "История списания устройств",
        "no_history": "Устройства не списывались"}


# Disposal
@register.inclusion_tag('decom/history_disp_short_list.html')
def disp_history_short():
    history_dev_list = HistoryDis.objects.all()[:5]

    return {
        "history_list": history_dev_list,
        "table_head": "История утилизации устройств",
        "no_history": "Устройства не утилизировались"}
