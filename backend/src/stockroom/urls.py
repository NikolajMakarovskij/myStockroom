from django.urls import include, path, re_path

from .routers import router
from .views.accessories import (
    AddToDeviceAccessoriesView,
    AddToStockAccessoriesView,
    ConsumptionAccRestView,
    ExportConsumptionAccessories,
    ExportConsumptionAccessoriesCategory,
    ExportStockAccessories,
    ExportStockAccessoriesCategory,
    HistoryAccDeviceFilterListRestView,
    HistoryAccFilterListRestView,
    RemoveFromStockAccessoriesView,
)
from .views.consumables import (
    AddToDeviceConsumableView,
    AddToStockConsumableView,
    ConsumptionRestView,
    ExportConsumptionConsumable,
    ExportConsumptionConsumableCategory,
    ExportStockConsumable,
    ExportStockConsumableCategory,
    HistoryConDeviceFilterListRestView,
    HistoryConFilterListRestView,
    RemoveFromStockConsumableView,
)
from .views.devices import (
    AddHistoryToDeviceView,
    AddToStockDeviceView,
    ExportStockDevice,
    ExportStockDeviceCategory,
    HistoryDevFilterListRestView,
    MoveDeviceView,
    RemoveFromStockDeviceView,
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
    re_path(
        "history_con_list/device/filter/(?P<deviceId>.+)/$",
        HistoryConDeviceFilterListRestView.as_view(),
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
    path(
        "consumption_acc_list/",
        ConsumptionAccRestView.as_view(),
        name="consumption_accessories_list",
    ),
    re_path(
        "history_acc_list/filter/(?P<stock_model_id>.+)/$",
        HistoryAccFilterListRestView.as_view(),
        name="stock_acc_model_filter",
    ),
    re_path(
        "history_acc_list/device/filter/(?P<deviceId>.+)/$",
        HistoryAccDeviceFilterListRestView.as_view(),
        name="stock_model_filter",
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
    # methods
    path(
        "add_to_stock_accessories/",
        AddToStockAccessoriesView.as_view(),
        name="add_to_stock_accessories",
    ),
    path(
        "add_to_device_accessories/",
        AddToDeviceAccessoriesView.as_view(),
        name="add_to_device_accessories",
    ),
    path(
        "remove_from_stock_accessories/",
        RemoveFromStockAccessoriesView.as_view(),
        name="remove_from_stock_accessories",
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
    re_path(
        "history_dev_list/filter/(?P<stock_model_id>.+)/$",
        HistoryDevFilterListRestView.as_view(),
        name="stock_dev_model_filter",
    ),
    path(
        "add_to_stock_device/",
        AddToStockDeviceView.as_view(),
        name="add_to_stock_device",
    ),
    path(
        "remove_from_stock_device/",
        RemoveFromStockDeviceView.as_view(),
        name="remove_from_stock_device",
    ),
    path(
        "move_device/",
        MoveDeviceView.as_view(),
        name="move_device",
    ),
    path(
        "add_device_history/",
        AddHistoryToDeviceView.as_view(),
        name="add_device_history",
    ),
    path("devices/export/", ExportStockDevice.as_view(), name="export_stock_device"),
    path(
        "devices/export/category/<slug:category_slug>",
        ExportStockDeviceCategory.as_view(),
        name="export_stock_device_category",
    ),
]
