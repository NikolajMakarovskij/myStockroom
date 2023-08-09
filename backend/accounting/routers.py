from .views import AccountingRestView, CategoriesRestView
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'accounting', AccountingRestView)
router.register(r'accounting_category', CategoriesRestView)