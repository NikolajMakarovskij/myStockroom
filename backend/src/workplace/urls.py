from django.urls import include, path, re_path

from .routers import router
from .views import (
    IndexView, RoomCreate, RoomDelete, RoomDetailView, RoomListView, RoomUpdate,
    WorkplaceCreate, WorkplaceDelete, WorkplaceDetailView, WorkplaceListView,
    WorkplaceUpdate,)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("", IndexView.as_view(), name="workplace_index"),
    # кабинеты
    path("room/", RoomListView.as_view(), name="room_list"),
    re_path(r"^room/search$", RoomListView.as_view(), name="room_search"),
    re_path(r"^room/(?P<pk>[-\w]+)$", RoomDetailView.as_view(), name="room-detail"),
    re_path(r"^room/create/$", RoomCreate.as_view(), name="new-room"),
    re_path(r"^room/(?P<pk>[-\w]+)/update$", RoomUpdate.as_view(), name="room-update"),
    re_path(r"^room/(?P<pk>[-\w]+)/delete$", RoomDelete.as_view(), name="room-delete"),
    # рабочие места
    path(r"workplace/", WorkplaceListView.as_view(), name="workplace_list"),
    re_path(
        r"^workplace/search$", WorkplaceListView.as_view(), name="workplace_search"
    ),
    re_path(
        r"^workplace/(?P<pk>[-\w]+)$",
        WorkplaceDetailView.as_view(),
        name="workplace-detail",
    ),
    re_path(r"^workplace/create/$", WorkplaceCreate.as_view(), name="new-workplace"),
    re_path(
        r"^workplace/(?P<pk>[-\w]+)/update$",
        WorkplaceUpdate.as_view(),
        name="workplace-update",
    ),
    re_path(
        r"^workplace/(?P<pk>[-\w]+)/delete$",
        WorkplaceDelete.as_view(),
        name="workplace-delete",
    ),
]
