from django.urls import path, re_path
from .views import *

urlpatterns = [
    #софт
    re_path(r'^$', softwareListView.as_view(), name='software'),
    re_path(r'^(?P<pk>[-\w]+)$', softwareDetailView.as_view(), name='software-detail'),
    path(r'^create$', softwareCreate.as_view(), name='new-software'),
    re_path(r'^(?P<pk>[-\w]+)/update$', softwareUpdate.as_view(), name='software-update'),
    re_path(r'^(?P<pk>[-\w]+)/delete$', softwareDelete.as_view(), name='software-delete'),
    #ОС
    re_path(r'^OS/$', OSListView.as_view(), name='OS'),
    re_path(r'^OS/(?P<pk>[-\w]+)$', OSDetailView.as_view(), name='OS-detail'),
    path(r'^OS/create$', OSCreate.as_view(), name='new-OS'),
    re_path(r'^OS/(?P<pk>[-\w]+)/update$', OSUpdate.as_view(), name='OS-update'),
    re_path(r'^OS/(?P<pk>[-\w]+)/delete$', OSDelete.as_view(), name='OS-delete'),
]