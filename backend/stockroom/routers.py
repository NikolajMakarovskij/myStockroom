from .views.consumables import StockRestView
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'stock', StockRestView)
#router.register(r'device_cat', DeviceCatRestView)
