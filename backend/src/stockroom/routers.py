from .views.consumables import StockRestView
from .views.devices import StockDevListRestView, StockDevCatListRestView
from rest_framework import routers

from .views.consumables import StockRestView

router = routers.SimpleRouter()
router.register(r'stock', StockRestView)
router.register(r'stock_dev_list', StockDevListRestView)
router.register(r'stock_dev_cat', StockDevCatListRestView)
