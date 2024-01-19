from .views import DeviceRestView, DeviceCatRestView, DeviceListRestView, DeviceListCatRestView
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'device', DeviceRestView)
router.register(r'device_list', DeviceListRestView)
router.register(r'device_category/<slug:slug>', DeviceListCatRestView)
router.register(r'device_cat', DeviceCatRestView)
