from .views import EmployeeRestView, EmployeeListRestView, PostRestView, PostListRestView, DepartamentRestView
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'departament', DepartamentRestView)
router.register(r'post', PostRestView)
router.register(r'employee', EmployeeRestView)
router.register(r'post_list', PostListRestView)
router.register(r'employee_list', EmployeeListRestView)