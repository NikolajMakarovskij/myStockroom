from .views import RoomRestView, WorkplaceRestView, WorkplaceListRestView, RoomListRestView
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'room', RoomRestView)
router.register(r'workplace', WorkplaceRestView)
router.register(r'room_list', RoomListRestView)
router.register(r'workplace_list', WorkplaceListRestView)