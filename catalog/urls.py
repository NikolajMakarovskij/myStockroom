from operator import index
from django.urls import path
from . import views
from django.urls import include, re_path


urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^workplace/$', views.WorkplaceListView.as_view(), name='workplace'),
    re_path(r'^employee/$', views.EmployeeListView.as_view(), name='employee'),
    re_path(r'^software/$', views.softwareListView.as_view(), name='software'),
    re_path(r'^workstation/$', views.workstationListView.as_view(), name='workstation'), 
    re_path(r'^workstation/(?P<pk>[-\w]+)$', views.workstationDetailView.as_view(), name='workstation-detail'),
    re_path(r'^printer/$', views.printerListView.as_view(), name='printer'),
    re_path(r'^printer/(?P<pk>[-\w]+)$', views.printerDetailView.as_view(), name='printer-detail'),
    re_path(r'^digital_signature/$', views.digitalSignatureListView.as_view(), name='digital-signature'),
    
]