from django.urls import path, re_path, include
from .routers import router
from .views import DeviceListView, DeviceCategoryListView, DeviceDetailView, DeviceCreate, DeviceUpdate, DeviceDelete

urlpatterns = [
    path('api/v1/', include(router.urls)),
    # устройства
    path('', DeviceListView.as_view(), name='device_list'),
    path('search', DeviceListView.as_view(), name='device_search'),
    path('category/<slug:category_slug>', DeviceCategoryListView.as_view(), name='category'),
    re_path(r'^(?P<pk>[-\w]+)$', DeviceDetailView.as_view(), name='device-detail'),
    re_path(r'^create/$', DeviceCreate.as_view(), name='new-device'),
    re_path(r'^(?P<pk>[-\w]+)/update$', DeviceUpdate.as_view(), name='device-update'),
    re_path(r'^(?P<pk>[-\w]+)/delete$', DeviceDelete.as_view(), name='device-delete'),
]
