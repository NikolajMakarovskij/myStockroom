from .views import *
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'device', DeviceRestView)
router.register(r'device_cat', Device_catRestView)