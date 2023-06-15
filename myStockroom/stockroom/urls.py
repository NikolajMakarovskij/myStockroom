from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', stockroomIndexView.as_view(), name='stock_index'),

    #Склад расходников
    re_path(r'^stockroom/$', stockroomView.as_view(), name='stock_list'),
    re_path(r'^stockroom/search$', stockroomView.as_view(), name='stock_search'),
    path('category/<slug:category_slug>', stockroomCategoriesView.as_view(), name='category'),

    path(r'^stockroom/add/(?P<consumable_id>\d+)/$', stock_add_consumable, name='stock_add_consumable'),
    path(r'^stockroom/remove/(?P<consumable_id>\d+)/$', stock_remove_consumable, name='stock_remove_consumable'),
    path(r'^stockroom/consumable/remove/(?P<consumable_id>\d+)/$', device_add_consumable, name='device_add_consumable'),

        
    re_path(r'^history$', HistoryView.as_view(), name='history_list'),
    re_path(r'^history/search$', HistoryView.as_view(), name='history_search'),
    path('history/category/<slug:category_slug>', HistoryCategoriesView.as_view(), name='history_category'),

    #Склад комплектующих
    re_path(r'^accessories/$', stockAccView.as_view(), name='stock_acc_list'),
    re_path(r'^accessories/search$', stockAccView.as_view(), name='stock_acc_search'),
    path('accessories/category/<slug:category_slug>', stockAccCategoriesView.as_view(), name='accessories_category'),

    path(r'^accessories/stockroom/add/(?P<accessories_id>\d+)/$', stock_add_accessories, name='stock_add_accessories'),
    path(r'^accessories/stockroom/remove/(?P<accessories_id>\d+)/$', stock_remove_accessories, name='stock_remove_accessories'),
    path(r'^accessories/stockroom/accessories/remove/(?P<accessories_id>\d+)/$', device_add_accessories, name='device_add_accessories'),

        
    re_path(r'^accessories/history$', HistoryAccView.as_view(), name='history_acc_list'),
    re_path(r'^accessories/history/search$', HistoryAccView.as_view(), name='history_acc_search'),
    path('accessories/history/category/<slug:category_slug>', HistoryAccCategoriesView.as_view(), name='history_acc_category'),

]