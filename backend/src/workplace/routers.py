from rest_framework import routers

from .views import RoomRestView, WorkplaceRestView

router = routers.SimpleRouter()
router.register(r'room', RoomRestView)
router.register(r'workplace', WorkplaceRestView)