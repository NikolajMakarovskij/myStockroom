from rest_framework import routers

from .views.consumables import (
    HistoryConListRestView,
    StockConCatListRestView,
    StockConListRestView,
)
from .views.devices import StockDevCatListRestView, StockDevListRestView

router = routers.SimpleRouter()
router.register(r"stock_con_list", StockConListRestView, basename="consumables_list")
router.register(
    r"stock_con_cat_list", StockConCatListRestView, basename="consumables_category_list"
)
router.register(
    r"history_con_list", HistoryConListRestView, basename="history_consumables_list"
)

router.register(r"stock_dev_list", StockDevListRestView, basename="device_list")
router.register(
    r"stock_dev_cat", StockDevCatListRestView, basename="device_category_list"
)
