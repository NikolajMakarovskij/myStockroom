from django.urls import path, re_path
from .views import EmployeeListView, EmployeeDetailView, EmployeeCreate, EmployeeUpdate, EmployeeDelete, PostListView, \
    PostDetailView, PostCreate, PostUpdate, PostDelete, DepartamentListView, DepartamentDetailView, DepartamentCreate, \
    DepartamentUpdate, DepartamentDelete

urlpatterns = [
    # сотрудники
    re_path(r'^$', EmployeeListView.as_view(), name='employee_list'),
    re_path(r'^search$', EmployeeListView.as_view(), name='employee_search'),
    re_path(r'^(?P<pk>[-\w]+)$', EmployeeDetailView.as_view(), name='employee-detail'),
    path(r'^create$', EmployeeCreate.as_view(), name='new-employee'),
    re_path(r'^(?P<pk>[-\w]+)/update$', EmployeeUpdate.as_view(), name='employee-update'),
    re_path(r'^(?P<pk>[-\w]+)/delete$', EmployeeDelete.as_view(), name='employee-delete'),

    # Должность
    re_path(r'^post/$', PostListView.as_view(), name='post_list'),
    re_path(r'^post/search$', PostListView.as_view(), name='post_search'),
    re_path(r'^post/(?P<pk>[-\w]+)$', PostDetailView.as_view(), name='post-detail'),
    path(r'^post/create$', PostCreate.as_view(), name='new-post'),
    re_path(r'^post/(?P<pk>[-\w]+)/update$', PostUpdate.as_view(), name='post-update'),
    re_path(r'^post/(?P<pk>[-\w]+)/delete$', PostDelete.as_view(), name='post-delete'),
    # Отдел
    re_path(r'^departament/$', DepartamentListView.as_view(), name='departament_list'),
    re_path(r'^departament/search$', DepartamentListView.as_view(), name='departament_search'),
    re_path(r'^departament/(?P<pk>[-\w]+)$', DepartamentDetailView.as_view(), name='departament-detail'),
    path(r'^departament/create$', DepartamentCreate.as_view(), name='new-departament'),
    re_path(r'^departament/(?P<pk>[-\w]+)/update$', DepartamentUpdate.as_view(), name='departament-update'),
    re_path(r'^departament/(?P<pk>[-\w]+)/delete$', DepartamentDelete.as_view(), name='departament-delete'),
]
