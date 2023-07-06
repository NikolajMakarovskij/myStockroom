from django.urls import path, re_path
from .views import SoftwareListView, SoftwareDetailView, SoftwareCreate, SoftwareUpdate, SoftwareDelete, OSListView, \
    OSDetailView, OSCreate, OSUpdate, OSDelete

urlpatterns = [
    # софт
    re_path(r'^$', SoftwareListView.as_view(), name='software_list'),
    re_path(r'^search$', SoftwareListView.as_view(), name='software_search'),
    re_path(r'^(?P<pk>[-\w]+)$', SoftwareDetailView.as_view(), name='software-detail'),
    path(r'^create$', SoftwareCreate.as_view(), name='new-software'),
    re_path(r'^(?P<pk>[-\w]+)/update$', SoftwareUpdate.as_view(), name='software-update'),
    re_path(r'^(?P<pk>[-\w]+)/delete$', SoftwareDelete.as_view(), name='software-delete'),
    # ОС
    re_path(r'^OS/$', OSListView.as_view(), name='OS_list'),
    re_path(r'^OS/search$', OSListView.as_view(), name='OS_search'),
    re_path(r'^OS/(?P<pk>[-\w]+)$', OSDetailView.as_view(), name='OS-detail'),
    path(r'^OS/create$', OSCreate.as_view(), name='new-OS'),
    re_path(r'^OS/(?P<pk>[-\w]+)/update$', OSUpdate.as_view(), name='OS-update'),
    re_path(r'^OS/(?P<pk>[-\w]+)/delete$', OSDelete.as_view(), name='OS-delete'),
]