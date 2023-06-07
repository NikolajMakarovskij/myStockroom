from django.urls import path, re_path, include
from .routers import *
from .views import *


urlpatterns = [  
    path('api/v1/', include(router.urls)),
    #устройства
    re_path(r'^$', deviceListView.as_view(), name='device_list'),
    re_path(r'^search$', deviceListView.as_view(), name='device_search'),
    path('category/<slug:category_slug>', deviceCategoryListView.as_view(), name='category'),
    re_path(r'^(?P<pk>[-\w]+)$', deviceDetailView.as_view(), name='device-detail'),
    path(r'^create$', deviceCreate.as_view(), name='new-device'),
    re_path(r'^(?P<pk>[-\w]+)/update$', deviceUpdate.as_view(), name='device-update'),
    re_path(r'^(?P<pk>[-\w]+)/delete$', deviceDelete.as_view(), name='device-delete'),
]