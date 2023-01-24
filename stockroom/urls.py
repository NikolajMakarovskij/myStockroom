from django.urls import path, re_path
from .views import *

urlpatterns = [
    path(r'^$', stock_detail, name='stock_detail'),
    path(r'^cartridge/add/(?P<cartridge_id>\d+)/$', stock_add_cartridge, name='stock_add_cartridge'),
    path(r'^cartridge/remove/(?P<cartridge_id>\d+)/$', stock_remove_cartridge, name='stock_remove_cartridge'),
    path(r'^toner/add/(?P<toner_id>\d+)/$', stock_add_toner, name='stock_add_toner'),
    path(r'^toner/remove/(?P<toner_id>\d+)/$', stock_remove_toner, name='stock_remove_toner'),
    path(r'^fotoval/add/(?P<fotoval_id>\d+)/$', stock_add_fotoval, name='stock_add_fotoval'),
    path(r'^fotoval/remove/(?P<fotoval_id>\d+)/$', stock_remove_fotoval, name='stock_remove_fotoval'),
    path(r'^accumulator/add/(?P<accumulator_id>\d+)/$', stock_add_accumulator, name='stock_add_accumulator'),
    path(r'^accumulator/remove/(?P<accumulator_id>\d+)/$', stock_remove_accumulator, name='stock_remove_accumulator'),
    path(r'^storage/add/(?P<storage_id>\d+)/$', stock_add_storage, name='stock_add_storage'),
    path(r'^storage/remove/(?P<storage_id>\d+)/$', stock_remove_storage, name='stock_remove_storage'),

    path(r'^printer/cartridge/remove/(?P<cartridge_id>\d+)/$', printer_add_cartridge, name='printer_add_cartridge'),
    path(r'^printer/toner/remove/(?P<toner_id>\d+)/$', printer_add_toner, name='printer_add_toner'),
    path(r'^printer/fotoval/remove/(?P<fotoval_id>\d+)/$', printer_add_fotoval, name='printer_add_fotoval'),
    path(r'^printer/accumulator/remove/(?P<accumulator_id>\d+)/$', ups_add_accumulator, name='ups_add_accumulator'),
    path(r'^printer/storage/remove/(?P<storage_id>\d+)/$', add_storage, name='add_storage'),

]