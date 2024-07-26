from django.urls import path, re_path

from .views import (
    IndexView, OSCreate, OSDelete, OSDetailView, OSListView, OSUpdate, SoftwareCreate,
    SoftwareDelete, SoftwareDetailView, SoftwareListView, SoftwareUpdate,)

urlpatterns = [
    path("", IndexView.as_view(), name="software_index"),
    # софт
    path("software/", SoftwareListView.as_view(), name="software_list"),
    path("software/search", SoftwareListView.as_view(), name="software_search"),
    re_path(
        r"^software/(?P<pk>[-\w]+)$",
        SoftwareDetailView.as_view(),
        name="software-detail",
    ),
    re_path(r"^software/create/$", SoftwareCreate.as_view(), name="new-software"),
    re_path(
        r"^software/(?P<pk>[-\w]+)/update$",
        SoftwareUpdate.as_view(),
        name="software-update",
    ),
    re_path(
        r"^software/(?P<pk>[-\w]+)/delete$",
        SoftwareDelete.as_view(),
        name="software-delete",
    ),
    # ОС
    path("OS/", OSListView.as_view(), name="OS_list"),
    path("OS/search", OSListView.as_view(), name="OS_search"),
    re_path(r"^OS/(?P<pk>[-\w]+)$", OSDetailView.as_view(), name="OS-detail"),
    re_path(r"^OS/create/$", OSCreate.as_view(), name="new-OS"),
    re_path(r"^OS/(?P<pk>[-\w]+)/update$", OSUpdate.as_view(), name="OS-update"),
    re_path(r"^OS/(?P<pk>[-\w]+)/delete$", OSDelete.as_view(), name="OS-delete"),
]
