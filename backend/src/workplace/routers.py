from rest_framework import routers

from .views import (
    RoomListRestView,
    RoomRestView,
    WorkplaceListRestView,
    WorkplaceRestView,
)

router = routers.SimpleRouter()
router.register(r"room", RoomRestView, basename="room_crud")
router.register(r"workplace", WorkplaceRestView, basename="workplace_crud")
router.register(r"room_list", RoomListRestView, basename="room_list")
router.register(r"workplace_list", WorkplaceListRestView, basename="workplace_list")
