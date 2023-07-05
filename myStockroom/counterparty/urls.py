from django.urls import path, re_path
from .views import CounterpartyView, ManufacturerListView, ManufacturerDetailView, ManufacturerCreate, \
    ManufacturerUpdate, ManufacturerDelete

urlpatterns = [
    re_path(r'^$', CounterpartyView.as_view(), name='counterparty'),
    # Производитель
    re_path(r'^manufacturer/$', ManufacturerListView.as_view(), name='manufacturer_list'),
    re_path(r'^manufacturer/search$', ManufacturerListView.as_view(), name='manufacturer_search'),
    re_path(r'^manufacturer/(?P<pk>[-\w]+)$', ManufacturerDetailView.as_view(), name='manufacturer-detail'),
    path(r'^manufacturer/create$', ManufacturerCreate.as_view(), name='new-manufacturer'),
    re_path(r'^manufacturer/(?P<pk>[-\w]+)/update$', ManufacturerUpdate.as_view(), name='manufacturer-update'),
    re_path(r'^manufacturer/(?P<pk>[-\w]+)/delete$', ManufacturerDelete.as_view(), name='manufacturer-delete'),
]
