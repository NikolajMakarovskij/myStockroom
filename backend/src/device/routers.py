from rest_framework import routers

from .views import DeviceCatRestView, DeviceListRestView, DeviceModelRestView

router = routers.SimpleRouter()
router.register(r"device_list", DeviceListRestView, basename="device_list")
router.register(r"device_crud", DeviceModelRestView, basename="device_crud")
router.register(r"device_cat", DeviceCatRestView, basename="device_cat")
