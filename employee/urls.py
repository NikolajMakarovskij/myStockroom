from django.urls import path, re_path
from .views import *

urlpatterns = [   
#сотрудники
    re_path(r'^$', EmployeeListView.as_view(), name='employee_list'),
    re_path(r'^search$', EmployeeListView.as_view(), name='employee_search'),
    re_path(r'^(?P<pk>[-\w]+)$', EmployeeDetailView.as_view(), name='employee-detail'),
    path(r'^create$', EmployeeCreate.as_view(), name='new-employee'),
    re_path(r'^(?P<pk>[-\w]+)/update$', EmployeeUpdate.as_view(), name='employee-update'),
    re_path(r'^(?P<pk>[-\w]+)/delete$', EmployeeDelete.as_view(), name='employee-delete'),

#Должность
    re_path(r'^post/$', postListView.as_view(), name='post_list'),
    re_path(r'^post/search$', postListView.as_view(), name='post_search'),
    re_path(r'^post/(?P<pk>[-\w]+)$', postDetailView.as_view(), name='post-detail'),
    path(r'^post/create$', postCreate.as_view(), name='new-post'),
    re_path(r'^post/(?P<pk>[-\w]+)/update$', postUpdate.as_view(), name='post-update'),
    re_path(r'^post/(?P<pk>[-\w]+)/delete$', postDelete.as_view(), name='post-delete'),
#Отдел
    re_path(r'^departament/$', departamentListView.as_view(), name='departament_list'),
    re_path(r'^departament/search$', departamentListView.as_view(), name='departament_search'),
    re_path(r'^departament/(?P<pk>[-\w]+)$', departamentDetailView.as_view(), name='departament-detail'),
    path(r'^departament/create$', departamentCreate.as_view(), name='new-departament'),
    re_path(r'^departament/(?P<pk>[-\w]+)/update$', departamentUpdate.as_view(), name='departament-update'),
    re_path(r'^departament/(?P<pk>[-\w]+)/delete$', departamentDelete.as_view(), name='departament-delete'),
]