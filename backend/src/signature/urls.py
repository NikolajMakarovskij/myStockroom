from django.urls import path, re_path
from .views import (
    SignatureListView,
    SignatureDetailView,
    SignatureCreate,
    SignatureUpdate,
    SignatureDelete,
)

urlpatterns = [
    # ЭЦП
    path("", SignatureListView.as_view(), name="signature_list"),
    path("search", SignatureListView.as_view(), name="signature_search"),
    re_path(
        r"^(?P<pk>[-\w]+)$", SignatureDetailView.as_view(), name="signature-detail"
    ),
    re_path(r"^create/$", SignatureCreate.as_view(), name="new-signature"),
    re_path(
        r"^(?P<pk>[-\w]+)/update$", SignatureUpdate.as_view(), name="signature-update"
    ),
    re_path(
        r"^(?P<pk>[-\w]+)/delete$", SignatureDelete.as_view(), name="signature-delete"
    ),
]
