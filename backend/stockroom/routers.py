from .views.consumables import StockRestView
from .views.devices import StockDevListRestView
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'stock', StockRestView)
router.register(r'stock_dev_list', StockDevListRestView)
