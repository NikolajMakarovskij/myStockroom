from rest_framework import routers

from .views.consumables import (
    HistoryConListRestView,
    StockConCatListRestView,
    StockConListRestView,
)
from .views.devices import StockDevCatListRestView, StockDevListRestView

router = routers.SimpleRouter()
router.register(r"stock_con_list", StockConListRestView)
router.register(r"stock_con_cat_list", StockConCatListRestView)
router.register(r"history_con_list", HistoryConListRestView)
router.register(r"stock_dev_list", StockDevListRestView)
router.register(r"stock_dev_cat", StockDevCatListRestView)
