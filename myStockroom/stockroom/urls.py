from django.urls import path, re_path
from .views import (
    StockroomIndexView, StockroomView, StockroomCategoriesView, stock_add_consumable, stock_remove_consumable,
    device_add_consumable, HistoryView, HistoryCategoriesView, StockAccView, StockAccCategoriesView,
    stock_add_accessories, stock_remove_accessories, device_add_accessories, HistoryAccView, HistoryAccCategoriesView,
    StockDevView, StockDevCategoriesView, stock_add_device, stock_remove_device, HistoryDevView,
    HistoryDevCategoriesView)

urlpatterns = [
    path('', StockroomIndexView.as_view(), name='stock_index'),

    # Склад расходников
    re_path(r'^stockroom/$', StockroomView.as_view(), name='stock_list'),
    re_path(r'^stockroom/search$', StockroomView.as_view(), name='stock_search'),
    path('category/<slug:category_slug>', StockroomCategoriesView.as_view(), name='category'),

    path(r'^stockroom/add/(?P<consumable_id>\d+)/$', stock_add_consumable, name='stock_add_consumable'),
    path(r'^stockroom/remove/(?P<consumable_id>\d+)/$', stock_remove_consumable, name='stock_remove_consumable'),
    path(r'^stockroom/consumable/remove/(?P<consumable_id>\d+)/$', device_add_consumable, name='device_add_consumable'),

    re_path(r'^history/$', HistoryView.as_view(), name='history_list'),
    re_path(r'^history/search$', HistoryView.as_view(), name='history_search'),
    path('history/category/<slug:category_slug>', HistoryCategoriesView.as_view(), name='history_category'),

    # Склад комплектующих
    re_path(r'^accessories/$', StockAccView.as_view(), name='stock_acc_list'),
    re_path(r'^accessories/search$', StockAccView.as_view(), name='stock_acc_search'),
    path('accessories/category/<slug:category_slug>', StockAccCategoriesView.as_view(), name='accessories_category'),

    path(r'^accessories/stockroom/add/(?P<accessories_id>\d+)/$', stock_add_accessories, name='stock_add_accessories'),
    path(r'^accessories/stockroom/remove/(?P<accessories_id>\d+)/$', stock_remove_accessories,
         name='stock_remove_accessories'),
    path(r'^accessories/stockroom/accessories/remove/(?P<accessories_id>\d+)/$', device_add_accessories,
         name='device_add_accessories'),

    re_path(r'^accessories/history/$', HistoryAccView.as_view(), name='history_acc_list'),
    re_path(r'^accessories/history/search$', HistoryAccView.as_view(), name='history_acc_search'),
    path('accessories/history/category/<slug:category_slug>', HistoryAccCategoriesView.as_view(),
         name='history_acc_category'),

    # Склад устройств
    re_path(r'^devices/$', StockDevView.as_view(), name='stock_dev_list'),
    re_path(r'^devices/search$', StockDevView.as_view(), name='stock_dev_search'),
    path('devices/category/<slug:category_slug>', StockDevCategoriesView.as_view(), name='devices_category'),

    path(r'^devices/stockroom/add/(?P<device_id>\d+)/$', stock_add_device, name='stock_add_device'),
    path(r'^devices/stockroom/remove/(?P<devices_id>\d+)/$', stock_remove_device, name='stock_remove_device'),
    # path(r'^devices/stockroom/move/(?P<device_id>\d+)/$', move_device, name='move_device'),

    re_path(r'^devices/history/$', HistoryDevView.as_view(), name='history_dev_list'),
    re_path(r'^devices/history/search$', HistoryDevView.as_view(), name='history_dev_search'),
    path('devices/history/category/<slug:category_slug>', HistoryDevCategoriesView.as_view(),
         name='history_dev_category'),

]
