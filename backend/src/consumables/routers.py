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
router.register(r"consumable", ConsumablesRestView, basename="consumables_crud")
router.register(
    r"consumable_list", ConsumablesListRestView, basename="consumables_list"
)
router.register(r"consumable_category", CategoriesRestView, basename="consumables_cat")
router.register(r"accessories", AccessoriesRestView, basename="accessories_crud")
router.register(
    r"accessories_list", AccessoriesListRestView, basename="accessories_list"
)
router.register(r"accessories_category", AccCatRestView, basename="accessories_cat")
