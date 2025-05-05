from django.urls import include, path

from .routers import router
from .views import (
    AddToDecommissionDeviceView,
    AddToDisposalDeviceView,
    ExportDecomDevice,
    ExportDecomDeviceCategory,
    ExportDispDevice,
    ExportDispDeviceCategory,
    RemoveFromDecommissionDeviceView,
    RemoveFromDisposalDeviceView,
)

urlpatterns = [
    path("", include(router.urls)),
    # Decommission
    # methods
    path(
        "add_to_decommission/",
        AddToDecommissionDeviceView.as_view(),
        name="add_to_decommission",
    ),
    path(
        "remove_from_decommission/",
        RemoveFromDecommissionDeviceView.as_view(),
        name="remove_from_decommission/",
    ),
    path("decom/export/", ExportDecomDevice.as_view(), name="export_decom_device"),
    path(
        "decom/export/category/<slug:category_slug>",
        ExportDecomDeviceCategory.as_view(),
        name="export_decom_device_category",
    ),
    # Disposal
    path(
        "add_to_disposal/",
        AddToDisposalDeviceView.as_view(),
        name="add_to_disposal",
    ),
    path(
        "remove_from_disposal/",
        RemoveFromDisposalDeviceView.as_view(),
        name="remove_from_disposal/",
    ),
    path("disposal/export/", ExportDispDevice.as_view(), name="export_disp_device"),
    path(
        "disposal/export/category/<slug:category_slug>",
        ExportDispDeviceCategory.as_view(),
        name="export_disp_device_category",
    ),
]
