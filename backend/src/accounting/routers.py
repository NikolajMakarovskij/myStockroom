from rest_framework import routers

from .views import AccountingRestView, CategoriesRestView

router = routers.SimpleRouter()
router.register(r"accounting", AccountingRestView)
router.register(r"accounting_category", CategoriesRestView)
