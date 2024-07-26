from django.urls import include, path, re_path

from .routers import router
from .views import (
    DeviceCategoryListView, DeviceCreate, DeviceDelete, DeviceDetailView,
    DeviceListView, DeviceUpdate, ExportDevice, ExportDeviceCategory,)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("", DeviceListView.as_view(), name="device_list"),
    path("search", DeviceListView.as_view(), name="device_search"),
    path(
        "category/<slug:category_slug>",
        DeviceCategoryListView.as_view(),
        name="category",
    ),
    path(
        "category/search/<slug:category_slug>",
        DeviceCategoryListView.as_view(),
        name="category_search",
    ),
    re_path(r"^(?P<pk>[-\w]+)$", DeviceDetailView.as_view(), name="device-detail"),
    re_path(r"^create/$", DeviceCreate.as_view(), name="new-device"),
    re_path(r"^(?P<pk>[-\w]+)/update$", DeviceUpdate.as_view(), name="device-update"),
    re_path(r"^(?P<pk>[-\w]+)/delete$", DeviceDelete.as_view(), name="device-delete"),
    path("export/", ExportDevice.as_view(), name="export_device"),
    path(
        "export/category/<slug:category_slug>",
        ExportDeviceCategory.as_view(),
        name="export_device_category",
    ),
]
