from rest_framework import routers

from .views.accessories import (
    HistoryAccListRestView,
    StockAccCatListRestView,
    StockAccListRestView,
)
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
router.register(r"stock_acc_list", StockAccListRestView, basename="accessories_list")
router.register(
    r"stock_acc_cat_list", StockAccCatListRestView, basename="accessories_category_list"
)
router.register(
    r"history_acc_list", HistoryAccListRestView, basename="history_accessories_list"
)
router.register(r"stock_dev_list", StockDevListRestView, basename="device_list")
router.register(
    r"stock_dev_cat", StockDevCatListRestView, basename="device_category_list"
)
