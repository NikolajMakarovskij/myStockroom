from django.urls import path, re_path, include
from .views import RoomListView, RoomCreate, RoomDetailView, RoomUpdate, RoomDelete, WorkplaceListView, \
    WorkplaceDetailView, WorkplaceCreate, WorkplaceUpdate, WorkplaceDelete
from .routers import router

urlpatterns = [
    path('api/v1/', include(router.urls)),
    # кабинеты
    path('room/', RoomListView.as_view(), name='room_list'),
    re_path(r'^room/search$', RoomListView.as_view(), name='room_search'),
    re_path(r'^room/(?P<pk>[-\w]+)$', RoomDetailView.as_view(), name='room-detail'),
    re_path(r'^room/create/$', RoomCreate.as_view(), name='new-room'),
    re_path(r'^room/(?P<pk>[-\w]+)/update$', RoomUpdate.as_view(), name='room-update'),
    re_path(r'^room/(?P<pk>[-\w]+)/delete$', RoomDelete.as_view(), name='room-delete'),
    # рабочие места
    path(r'', WorkplaceListView.as_view(), name='workplace_list'),
    re_path(r'^search$', WorkplaceListView.as_view(), name='workplace_search'),
    re_path(r'^(?P<pk>[-\w]+)$', WorkplaceDetailView.as_view(), name='workplace-detail'),
    re_path(r'^create/$', WorkplaceCreate.as_view(), name='new-workplace'),
    re_path(r'^(?P<pk>[-\w]+)/update$', WorkplaceUpdate.as_view(), name='workplace-update'),
    re_path(r'^(?P<pk>[-\w]+)/delete$', WorkplaceDelete.as_view(), name='workplace-delete'),
]
