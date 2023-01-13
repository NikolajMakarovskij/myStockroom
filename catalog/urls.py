from django.urls import path, re_path
from .views import *

urlpatterns = [
    #главная
    re_path(r'^$', indexView.as_view(), name='index'),
    #справочники
    re_path(r'^references/$', referencesView.as_view(), name='references'),
    #склад
    re_path(r'^warehouse/$', warehouseView.as_view(), name='warehouse'),
 
    #Производитель
    re_path(r'^manufacturer/$', manufacturerListView.as_view(), name='manufacturer'),
    re_path(r'^manufacturer/(?P<pk>[-\w]+)$', manufacturerDetailView.as_view(), name='manufacturer-detail'),
    path(r'^manufacturer/create$', manufacturerCreate.as_view(), name='new-manufacturer'),
    re_path(r'^manufacturer/(?P<pk>[-\w]+)/update$', manufacturerUpdate.as_view(), name='manufacturer-update'),
    re_path(r'^manufacturer/(?P<pk>[-\w]+)/delete$', manufacturerDelete.as_view(), name='manufacturer-delete'),
    #Накопитель
    re_path(r'^storage/$', storageListView.as_view(), name='storage'),
    re_path(r'^storage/(?P<pk>[-\w]+)$', storageDetailView.as_view(), name='storage-detail'),
    path(r'^storage/create$', storageCreate.as_view(), name='new-storage'),
    re_path(r'^storage/(?P<pk>[-\w]+)/update$', storageUpdate.as_view(), name='storage-update'),
    re_path(r'^storage/(?P<pk>[-\w]+)/delete$', storageDelete.as_view(), name='storage-delete'),


]