from django.urls import path, re_path
from .views import *

urlpatterns = [    
    #кабинеты
    re_path(r'^room/$', RoomListView.as_view(), name='room_list'),
    re_path(r'^room/api/$', RoomRestView.as_view(), name='api_room'),
    re_path(r'^room/search$', RoomListView.as_view(), name='room_search'),
    path(r'^room/(?P<pk>[-\w]+)$', RoomDetailView.as_view(), name='room-detail'),
    path(r'^room/create$', RoomCreate.as_view(), name='new-room'),
    re_path(r'^room/(?P<pk>[-\w]+)/update$', RoomUpdate.as_view(), name='room-update'),
    re_path(r'^room/(?P<pk>[-\w]+)/delete$', RoomDelete.as_view(), name='room-delete'),
    #рабочие места
    re_path(r'^$', WorkplaceListView.as_view(), name='workplace_list'),
    re_path(r'^api/$', WorkplaceRestView.as_view(), name='api_workplace'),
    re_path(r'^search$', WorkplaceListView.as_view(), name='workplace_search'),
    path(r'^(?P<pk>[-\w]+)$', WorkplaceDetailView.as_view(), name='workplace-detail'),
    path(r'^create$', WorkplaceCreate.as_view(), name='new-workplace'),
    re_path(r'^(?P<pk>[-\w]+)/update$', WorkplaceUpdate.as_view(), name='workplace-update'),
    re_path(r'^(?P<pk>[-\w]+)/delete$', WorkplaceDelete.as_view(), name='workplace-delete'),
]