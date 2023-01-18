from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path(r'^$', consumablesView.as_view(), name='consumables'),
    #картриджы
    re_path(r'^cartridge/$', cartridgeListView.as_view(), name='cartridge_list'),
    re_path(r'^cartridge/(?P<pk>[-\w]+)$', cartridgeDetailView.as_view(), name='cartridge-detail'),
    path(r'^cartridge/create$', cartridgeCreate.as_view(), name='new-cartridge'),
    re_path(r'^cartridge/(?P<pk>[-\w]+)/update$', cartridgeUpdate.as_view(), name='cartridge-update'),
    re_path(r'^cartridge/(?P<pk>[-\w]+)/delete$', cartridgeDelete.as_view(), name='cartridge-delete'),
    #фотовалы
    re_path(r'^fotoval/$', fotovalListView.as_view(), name='fotoval_list'),
    re_path(r'^fotoval/(?P<pk>[-\w]+)$', fotovalDetailView.as_view(), name='fotoval-detail'),
    path(r'^fotoval/create$', fotovalCreate.as_view(), name='new-fotoval'),
    re_path(r'^fotoval/(?P<pk>[-\w]+)/update$', fotovalUpdate.as_view(), name='fotoval-update'),
    re_path(r'^fotoval/(?P<pk>[-\w]+)/delete$', fotovalDelete.as_view(), name='fotoval-delete'),
    #Тонеры
    re_path(r'^toner/$', tonerListView.as_view(), name='toner_list'),
    re_path(r'^toner/(?P<pk>[-\w]+)$', tonerDetailView.as_view(), name='toner-detail'),
    path(r'^toner/create$', tonerCreate.as_view(), name='new-toner'),
    re_path(r'^toner/(?P<pk>[-\w]+)/update$', tonerUpdate.as_view(), name='toner-update'),
    re_path(r'^toner/(?P<pk>[-\w]+)/delete$', tonerDelete.as_view(), name='toner-delete'),
    #Аккумулятор
    re_path(r'^accumulator/$', accumulatorListView.as_view(), name='accumulator_list'),
    re_path(r'^accumulator/(?P<pk>[-\w]+)$', accumulatorDetailView.as_view(), name='accumulator-detail'),
    path(r'^accumulator/create$', accumulatorCreate.as_view(), name='new-accumulator'),
    re_path(r'^accumulator/(?P<pk>[-\w]+)/update$', accumulatorUpdate.as_view(), name='accumulator-update'),
    re_path(r'^accumulator/(?P<pk>[-\w]+)/delete$', accumulatorDelete.as_view(), name='accumulator-delete'),
    #Накопитель
    re_path(r'^storage/$', storageListView.as_view(), name='storage_list'),
    re_path(r'^storage/(?P<pk>[-\w]+)$', storageDetailView.as_view(), name='storage-detail'),
    path(r'^storage/create$', storageCreate.as_view(), name='new-storage'),
    re_path(r'^storage/(?P<pk>[-\w]+)/update$', storageUpdate.as_view(), name='storage-update'),
    re_path(r'^storage/(?P<pk>[-\w]+)/delete$', storageDelete.as_view(), name='storage-delete'),
]