from rest_framework import routers

from .views.consumables import StockRestView

router = routers.SimpleRouter()
router.register(r'stock', StockRestView)
#router.register(r'device_cat', DeviceCatRestView)
