from rest_framework import routers

from .views import (
    DepartamentRestView,
    EmployeeListRestView,
    EmployeeRestView,
    PostListRestView,
    PostRestView,
)

router = routers.SimpleRouter()
router.register(r"departament", DepartamentRestView)
router.register(r"post", PostRestView, basename="post_crud")
router.register(r"employee", EmployeeRestView, basename="employee_crud")
router.register(r"post_list", PostListRestView, basename="post_list")
router.register(r"employee_list", EmployeeListRestView, basename="employee_list")
