from rest_framework import routers

from .views import (
    DecommissionCatListRestView,
    DecommissionListRestView,
    DisposalCatListRestView,
    DisposalListRestView,
)

router = routers.SimpleRouter()
router.register(
    r"decommission_list", DecommissionListRestView, basename="decommission_list"
)
router.register(
    r"decommission_cat_list",
    DecommissionCatListRestView,
    basename="decommission_cat_list",
)
router.register(r"disposal_list", DisposalListRestView, basename="disposal_list")
router.register(
    r"disposal_cat_list", DisposalCatListRestView, basename="disposal_cat_list"
)
