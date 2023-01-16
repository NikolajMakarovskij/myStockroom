from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path(r'^$', CounterpartyView.as_view(), name='counterparty'),
    #Производитель
    re_path(r'^manufacturer/$', manufacturerListView.as_view(), name='manufacturer'),
    re_path(r'^manufacturer/(?P<pk>[-\w]+)$', manufacturerDetailView.as_view(), name='manufacturer-detail'),
    path(r'^manufacturer/create$', manufacturerCreate.as_view(), name='new-manufacturer'),
    re_path(r'^manufacturer/(?P<pk>[-\w]+)/update$', manufacturerUpdate.as_view(), name='manufacturer-update'),
    re_path(r'^manufacturer/(?P<pk>[-\w]+)/delete$', manufacturerDelete.as_view(), name='manufacturer-delete'),
]