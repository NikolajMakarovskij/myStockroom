from rest_framework import routers

from .views import AccountingListRestView, AccountingRestView, CategoriesRestView

router = routers.SimpleRouter()
router.register(r"accounting", AccountingRestView, basename="accounting_crud")
router.register(r"accounting_list", AccountingListRestView, basename="accounting_list")
router.register(r"accounting_category", CategoriesRestView, basename="accounting_cat")
