from django.urls import path, include
from .routers import router
from stockroom.views.accessories import StockAccView, StockAccCategoriesView, stock_add_accessories, \
    stock_remove_accessories, device_add_accessories, HistoryAccView, HistoryAccCategoriesView, \
    HistoryConsumptionAccView, HistoryAccConsumptionCategoriesView
from stockroom.views.devices import StockDevView, StockDevCategoriesView, stock_add_device, stock_remove_device, \
    HistoryDevView, HistoryDevCategoriesView, move_device_from_stock, add_history_to_device
from stockroom.views.index import StockroomIndexView
from stockroom.views.consumables import StockroomView, StockroomCategoriesView, stock_add_consumable, \
    stock_remove_consumable, device_add_consumable, HistoryView, HistoryCategoriesView, HistoryConsumptionView, \
    HistoryConsumptionCategoriesView


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('', StockroomIndexView.as_view(), name='stock_index'),

    # Consumables
    path('stockroom/', StockroomView.as_view(), name='stock_list'),
    path('stockroom/search', StockroomView.as_view(), name='stock_search'),
    path('category/<slug:category_slug>', StockroomCategoriesView.as_view(), name='category'),

    path('stockroom/add/<uuid:consumable_id>/', stock_add_consumable, name='stock_add_consumable'),
    path('stockroom/remove/<uuid:consumable_id>/', stock_remove_consumable, name='stock_remove_consumable'),
    path('stockroom/consumable/remove/<uuid:consumable_id>/', device_add_consumable, name='device_add_consumable'),

    path('history/', HistoryView.as_view(), name='history_list'),
    path('history/search', HistoryView.as_view(), name='history_search'),
    path('history/category/<slug:category_slug>', HistoryCategoriesView.as_view(), name='history_category'),
    path('history/consumption/', HistoryConsumptionView.as_view(), name='history_consumption_list'),
    path('history/consumption/search', HistoryConsumptionView.as_view(), name='history_consumption_search'),
    path('history/consumption/category/<slug:category_slug>', HistoryConsumptionCategoriesView.as_view(),
         name='history_consumption_category'),


    # Accessories
    path('accessories/', StockAccView.as_view(), name='stock_acc_list'),
    path('accessories/search', StockAccView.as_view(), name='stock_acc_search'),
    path('accessories/category/<slug:category_slug>', StockAccCategoriesView.as_view(), name='accessories_category'),

    path('accessories/stockroom/add/<uuid:accessories_id>/', stock_add_accessories, name='stock_add_accessories'),
    path('accessories/stockroom/remove/<uuid:accessories_id>/', stock_remove_accessories,
         name='stock_remove_accessories'),
    path('accessories/stockroom/accessories/remove/<uuid:accessories_id>/', device_add_accessories,
         name='device_add_accessories'),

    path('accessories/history/', HistoryAccView.as_view(), name='history_acc_list'),
    path('accessories/history/search', HistoryAccView.as_view(), name='history_acc_search'),
    path('accessories/history/category/<slug:category_slug>', HistoryAccCategoriesView.as_view(),
         name='history_acc_category'),
    path('accessories/consumption/', HistoryConsumptionAccView.as_view(), name='history_consumption_acc_list'),
    path('accessories/consumption/search', HistoryConsumptionAccView.as_view(), name='history_consumption_acc_search'),
    path('accessories/consumption/category/<slug:category_slug>', HistoryAccConsumptionCategoriesView.as_view(),
         name='history_acc_consumption_category'),

    # Devices
    path('devices/', StockDevView.as_view(), name='stock_dev_list'),
    path('devices/search', StockDevView.as_view(), name='stock_dev_search'),
    path('devices/category/<slug:category_slug>', StockDevCategoriesView.as_view(), name='devices_category'),

    path('devices/stockroom/add/<uuid:device_id>/', stock_add_device, name='stock_add_device'),
    path('devices/stockroom/remove/<uuid:devices_id>/', stock_remove_device, name='stock_remove_device'),


    path('devices/history/', HistoryDevView.as_view(), name='history_dev_list'),
    path('devices/history/search', HistoryDevView.as_view(), name='history_dev_search'),
    path('devices/history/category/<slug:category_slug>', HistoryDevCategoriesView.as_view(),
         name='history_dev_category'),
    path('devices/stockroom/move/<uuid:device_id>/', move_device_from_stock, name='move_device'),
    path('devices/stockroom/add_history/<uuid:device_id>/', add_history_to_device, name='add_device_history'),
]
