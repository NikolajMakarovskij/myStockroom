from django.urls import path
from .views import *

urlpatterns = [
    path(r'^$', stock_detail, name='stock_detail'),
    path(r'^add/(?P<cartridge_id>\d+)/$', stock_add, name='stock_add'),
    path(r'^remove/(?P<cartridge_id>\d+)/$', stock_remove, name='stock_remove'),
]