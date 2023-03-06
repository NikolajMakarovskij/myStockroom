from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path(r'^$', stockroomView.as_view(), name='stock_list'),
    re_path(r'^search$', stockroomView.as_view(), name='stock_search'),
    path('category/<slug:category_slug>', stockroomCategoriesView.as_view(), name='category'),

    path(r'^stockroom/add/(?P<consumable_id>\d+)/$', stock_add_consumable, name='stock_add_consumable'),
    path(r'^stockroom/remove/(?P<consumable_id>\d+)/$', stock_remove_consumable, name='stock_remove_consumable'),
    path(r'^stockroom/consumable/remove/(?P<consumable_id>\d+)/$', device_add_consumable, name='device_add_consumable'),

]