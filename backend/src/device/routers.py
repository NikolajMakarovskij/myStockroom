from rest_framework import routers

from .views import DeviceCatRestView, DeviceRestView

router = routers.SimpleRouter()
router.register(r'device', DeviceRestView)
router.register(r'device_cat', DeviceCatRestView)
