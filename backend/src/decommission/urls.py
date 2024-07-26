from django.urls import path

from .views import (
    DecomCategoriesView, DecommissionView, DispCategoriesView, DisposalView,
    ExportDecomDevice, ExportDecomDeviceCategory, ExportDispDevice,
    ExportDispDeviceCategory, add_decommission, add_disposal, remove_decommission,
    remove_disposal,)

urlpatterns = [
    # Decommission
    path("decom/", DecommissionView.as_view(), name="decom_list"),
    path("decom/search", DecommissionView.as_view(), name="decom_search"),
    path(
        "decom/category/<slug:category_slug>",
        DecomCategoriesView.as_view(),
        name="decom_category",
    ),
    path("decom/add/<uuid:device_id>/", add_decommission, name="add_decom"),
    path("decom/remove/<uuid:devices_id>/", remove_decommission, name="remove_decom"),
    path("decom/export/", ExportDecomDevice.as_view(), name="export_decom_device"),
    path(
        "decom/export/category/<slug:category_slug>",
        ExportDecomDeviceCategory.as_view(),
        name="export_decom_device_category",
    ),
    # Disposal
    path("disposal/", DisposalView.as_view(), name="disp_list"),
    path("disposal/search", DisposalView.as_view(), name="disp_search"),
    path(
        "disposal/category/<slug:category_slug>",
        DispCategoriesView.as_view(),
        name="disp_category",
    ),
    path("disposal/add/<uuid:devices_id>/", add_disposal, name="add_disp"),
    path("disposal/remove/<uuid:devices_id>/", remove_disposal, name="remove_disp"),
    path("disposal/export/", ExportDispDevice.as_view(), name="export_disp_device"),
    path(
        "disposal/export/category/<slug:category_slug>",
        ExportDispDeviceCategory.as_view(),
        name="export_disp_device_category",
    ),
]
