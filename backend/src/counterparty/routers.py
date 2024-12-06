from .views import ManufacturerRestView
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r"manufacturer", ManufacturerRestView)
