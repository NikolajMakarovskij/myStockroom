from rest_framework import routers

from .views import DeviceCatRestView, DeviceListRestView, DeviceRestView

router = routers.SimpleRouter()
router.register(r"device", DeviceRestView)
router.register(r"device_list", DeviceListRestView)
router.register(r"device_cat", DeviceCatRestView)
