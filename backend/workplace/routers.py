from .views import RoomRestView, WorkplaceRestView
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'room', RoomRestView)
router.register(r'workplace', WorkplaceRestView)