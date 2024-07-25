from .views import AccountingRestView, CategoriesRestView, AccountingListRestView
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'accounting', AccountingRestView)
router.register(r'accounting_list', AccountingListRestView)
router.register(r'accounting_category', CategoriesRestView)