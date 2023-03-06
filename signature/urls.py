from django.urls import path, re_path
from .views import *

urlpatterns = [
    #ЭЦП
    re_path(r'^$', signatureListView.as_view(), name='signature_list'),
    re_path(r'^search$', signatureListView.as_view(), name='signature_search'),
    re_path(r'^(?P<pk>[-\w]+)$', signatureDetailView.as_view(), name='signature-detail'),
    path(r'^create$', signatureCreate.as_view(), name='new-signature'),
    re_path(r'^(?P<pk>[-\w]+)/update$', signatureUpdate.as_view(), name='signature-update'),
    re_path(r'^(?P<pk>[-\w]+)/delete$', signatureDelete.as_view(), name='signature-delete'),
]