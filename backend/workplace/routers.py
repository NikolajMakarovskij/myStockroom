from .views import *
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'room', RoomRestView)
router.register(r'workplace', WorkplaceRestView)