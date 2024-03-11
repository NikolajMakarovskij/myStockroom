from .views import (CategoriesRestView, ConsumablesRestView, ConsumablesListRestView,
                    AccessoriesRestView, AccCatRestView, AccessoriesListRestView)
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'consumable', ConsumablesRestView)
router.register(r'consumable_list', ConsumablesListRestView)
router.register(r'consumable_category', CategoriesRestView)
router.register(r'accessories', AccessoriesRestView)
router.register(r'accessories_list', AccessoriesListRestView)
router.register(r'accessories_category', AccCatRestView)
