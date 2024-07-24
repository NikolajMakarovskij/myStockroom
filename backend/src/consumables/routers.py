from rest_framework import routers

from .views import (
    AccCatRestView,
    AccessoriesListRestView,
    AccessoriesRestView,
    CategoriesRestView,
    ConsumablesListRestView,
    ConsumablesRestView,
)

router = routers.SimpleRouter()
router.register(r"consumable", ConsumablesRestView)
router.register(r"consumable_list", ConsumablesListRestView)
router.register(r"consumable_category", CategoriesRestView)
router.register(r"accessories", AccessoriesRestView)
router.register(r"accessories_list", AccessoriesListRestView)
router.register(r"accessories_category", AccCatRestView)
