from django.urls import path, re_path
from .views import *

urlpatterns = [   
    #ИБП
    re_path(r'^$', upsListView.as_view(), name='ups_list'),
    re_path(r'^search$', upsListView.as_view(), name='ups_search'),
    re_path(r'^(?P<pk>[-\w]+)$', upsDetailView.as_view(), name='ups-detail'),
    path(r'^create$', upsCreate.as_view(), name='new-ups'),
    re_path(r'^(?P<pk>[-\w]+)/update$', upsUpdate.as_view(), name='ups-update'),
    re_path(r'^(?P<pk>[-\w]+)/delete$', upsDelete.as_view(), name='ups-delete'),
    #Кассеты
    re_path(r'^cassette/$', cassetteListView.as_view(), name='cassette_list'),
    re_path(r'^cassette/search$', cassetteListView.as_view(), name='cassette_search'),
    re_path(r'^cassette/(?P<pk>[-\w]+)$', cassetteDetailView.as_view(), name='cassette-detail'),
    path(r'^cassette/create$', cassetteCreate.as_view(), name='new-cassette'),
    re_path(r'^cassette/(?P<pk>[-\w]+)/update$', cassetteUpdate.as_view(), name='cassette-update'),
    re_path(r'^cassette/(?P<pk>[-\w]+)/delete$', cassetteDelete.as_view(), name='cassette-delete'),
]