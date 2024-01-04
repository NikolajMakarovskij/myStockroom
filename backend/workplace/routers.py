from .views import RoomRestView, WorkplaceRestView, WorkplaceListRestView
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'room', RoomRestView)
router.register(r'workplace', WorkplaceRestView)
router.register(r'workplace_list', WorkplaceListRestView)