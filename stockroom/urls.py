from django.urls import path, re_path
from .views import *

urlpatterns = [
    path(r'^$', stock, name='stock'),
    
    path(r'^stockroom/add/(?P<consumable_id>\d+)/$', stock_add_consumable, name='stock_add_consumable'),
    path(r'^stockroom/remove/(?P<consumable_id>\d+)/$', stock_remove_consumable, name='stock_remove_consumable'),
    path(r'^stockroom/consumable/remove/(?P<consumable_id>\d+)/$', printer_add_consumable, name='device_add_consumable'),

]