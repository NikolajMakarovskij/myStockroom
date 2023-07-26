from django.urls import path, re_path
from .views import EmployeeListView, EmployeeDetailView, EmployeeCreate, EmployeeUpdate, EmployeeDelete, PostListView, \
    PostDetailView, PostCreate, PostUpdate, PostDelete, DepartamentListView, DepartamentDetailView, DepartamentCreate, \
    DepartamentUpdate, DepartamentDelete, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='employee_index'),
    # сотрудники
    path('employee/', EmployeeListView.as_view(), name='employee_list'),
    path('employee/search', EmployeeListView.as_view(), name='employee_search'),
    re_path(r'^employee/(?P<pk>[-\w]+)$', EmployeeDetailView.as_view(), name='employee-detail'),
    re_path(r'^employee/create/$', EmployeeCreate.as_view(), name='new-employee'),
    re_path(r'^employee/(?P<pk>[-\w]+)/update$', EmployeeUpdate.as_view(), name='employee-update'),
    re_path(r'^employee/(?P<pk>[-\w]+)/delete$', EmployeeDelete.as_view(), name='employee-delete'),

    # Должность
    path('post/', PostListView.as_view(), name='post_list'),
    path('post/search', PostListView.as_view(), name='post_search'),
    re_path(r'^post/(?P<pk>[-\w]+)$', PostDetailView.as_view(), name='post-detail'),
    re_path(r'^post/create/$', PostCreate.as_view(), name='new-post'),
    re_path(r'^post/(?P<pk>[-\w]+)/update$', PostUpdate.as_view(), name='post-update'),
    re_path(r'^post/(?P<pk>[-\w]+)/delete$', PostDelete.as_view(), name='post-delete'),
    # Отдел
    path('departament/', DepartamentListView.as_view(), name='departament_list'),
    path('departament/search', DepartamentListView.as_view(), name='departament_search'),
    re_path(r'^departament/(?P<pk>[-\w]+)$', DepartamentDetailView.as_view(), name='departament-detail'),
    re_path(r'^departament/create/$', DepartamentCreate.as_view(), name='new-departament'),
    re_path(r'^departament/(?P<pk>[-\w]+)/update$', DepartamentUpdate.as_view(), name='departament-update'),
    re_path(r'^departament/(?P<pk>[-\w]+)/delete$', DepartamentDelete.as_view(), name='departament-delete'),
]
