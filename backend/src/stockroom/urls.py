from django.urls import include, path, re_path

from .routers import router
from .views.accessories import (
    ExportConsumptionAccessories,
    ExportConsumptionAccessoriesCategory,
    ExportStockAccessories,
    ExportStockAccessoriesCategory,
    HistoryAccCategoriesView,
    HistoryAccConsumptionCategoriesView,
    HistoryAccView,
    HistoryConsumptionAccView,
    StockAccCategoriesView,
    StockAccView,
    device_add_accessories,
    stock_add_accessories,
    stock_remove_accessories,
)
from .views.consumables import (
    AddToDeviceConsumableView,
    AddToStockConsumableView,
    ConsumptionRestView,
    ExportConsumptionConsumable,
    ExportConsumptionConsumableCategory,
    ExportStockConsumable,
    ExportStockConsumableCategory,
    HistoryConFilterListRestView,
    RemoveFromStockConsumableView,
)
from .views.devices import (
    ExportStockDevice,
    ExportStockDeviceCategory,
    HistoryDevCategoriesView,
    HistoryDevView,
    StockDevCategoriesView,
    StockDevView,
    add_history_to_device,
    move_device_from_stock,
    stock_add_device,
    stock_remove_device,
)
from .views.index import StockroomIndexView

urlpatterns = [
    path("", include(router.urls)),
    path("", StockroomIndexView.as_view(), name="stock_index"),
    # Consumables
    path(
        "consumption_con_list/",
        ConsumptionRestView.as_view(),
        name="consumption_consumables_list",
    ),
    re_path(
        "history_con_list/filter/(?P<stock_model_id>.+)/$",
        HistoryConFilterListRestView.as_view(),
        name="stock_model_filter",
    ),
    path(
        "stockroom/export/",
        ExportStockConsumable.as_view(),
        name="export_stock_consumable",
    ),
    path(
        "stockroom/export/category/<slug:category_slug>",
        ExportStockConsumableCategory.as_view(),
        name="export_stock_consumable_category",
    ),
    # methods
    path(
        "add_to_stock_consumable/",
        AddToStockConsumableView.as_view(),
        name="add_to_stock_consumable",
    ),
    path(
        "add_to_device_consumable/",
        AddToDeviceConsumableView.as_view(),
        name="add_to_device_consumable",
    ),
    path(
        "remove_from_stock_consumable/",
        RemoveFromStockConsumableView.as_view(),
        name="remove_from_stock_consumable",
    ),
    # history
    path(
        "stockroom/history/export/",
        ExportConsumptionConsumable.as_view(),
        name="export_consumption_consumable",
    ),
    path(
        "stockroom/history/export/category/<slug:category_slug>",
        ExportConsumptionConsumableCategory.as_view(),
        name="export_consumption_consumable_category",
    ),
    # Accessories
    path("accessories/", StockAccView.as_view(), name="stock_acc_list"),
    path("accessories/search", StockAccView.as_view(), name="stock_acc_search"),
    path(
        "accessories/category/<slug:category_slug>",
        StockAccCategoriesView.as_view(),
        name="accessories_category",
    ),
    path(
        "accessories/export/",
        ExportStockAccessories.as_view(),
        name="export_stock_accessories",
    ),
    path(
        "accessories/export/category/<slug:category_slug>",
        ExportStockAccessoriesCategory.as_view(),
        name="export_stock_accessories_category",
    ),
    path(
        "accessories/stockroom/add/<uuid:accessories_id>/",
        stock_add_accessories,
        name="stock_add_accessories",
    ),
    path(
        "accessories/stockroom/remove/<uuid:accessories_id>/",
        stock_remove_accessories,
        name="stock_remove_accessories",
    ),
    path(
        "accessories/stockroom/accessories/remove/<uuid:accessories_id>/",
        device_add_accessories,
        name="device_add_accessories",
    ),
    path("accessories/history/", HistoryAccView.as_view(), name="history_acc_list"),
    path(
        "accessories/history/search",
        HistoryAccView.as_view(),
        name="history_acc_search",
    ),
    path(
        "accessories/history/category/<slug:category_slug>",
        HistoryAccCategoriesView.as_view(),
        name="history_acc_category",
    ),
    path(
        "accessories/consumption/",
        HistoryConsumptionAccView.as_view(),
        name="history_consumption_acc_list",
    ),
    path(
        "accessories/consumption/search",
        HistoryConsumptionAccView.as_view(),
        name="history_consumption_acc_search",
    ),
    path(
        "accessories/consumption/category/<slug:category_slug>",
        HistoryAccConsumptionCategoriesView.as_view(),
        name="history_acc_consumption_category",
    ),
    path(
        "accessories/consumption/export/",
        ExportConsumptionAccessories.as_view(),
        name="export_consumption_acc",
    ),
    path(
        "accessories/consumption/export/category/<slug:category_slug>",
        ExportConsumptionAccessoriesCategory.as_view(),
        name="export_consumption_acc_category",
    ),
    # Devices
    path("devices/", StockDevView.as_view(), name="stock_dev_list"),
    path("devices/search", StockDevView.as_view(), name="stock_dev_search"),
    path(
        "devices/category/<slug:category_slug>",
        StockDevCategoriesView.as_view(),
        name="devices_category",
    ),
    path(
        "devices/stockroom/add/<uuid:device_id>/",
        stock_add_device,
        name="stock_add_device",
    ),
    path(
        "devices/stockroom/remove/<uuid:devices_id>/",
        stock_remove_device,
        name="stock_remove_device",
    ),
    path("devices/history/", HistoryDevView.as_view(), name="history_dev_list"),
    path("devices/history/search", HistoryDevView.as_view(), name="history_dev_search"),
    path(
        "devices/history/category/<slug:category_slug>",
        HistoryDevCategoriesView.as_view(),
        name="history_dev_category",
    ),
    path(
        "devices/stockroom/move/<uuid:device_id>/",
        move_device_from_stock,
        name="move_device",
    ),
    path(
        "devices/stockroom/add_history/<uuid:device_id>/",
        add_history_to_device,
        name="add_device_history",
    ),
    path("devices/export/", ExportStockDevice.as_view(), name="export_stock_device"),
    path(
        "devices/export/category/<slug:category_slug>",
        ExportStockDeviceCategory.as_view(),
        name="export_stock_device_category",
    ),
]
