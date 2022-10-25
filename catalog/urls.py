from operator import index
from django.urls import path
from .views import views
from django.urls import include, re_path


urlpatterns = [
    #главная
    re_path(r'^$', views.indexView.as_view(), name='index'),
    #кабинеты
    re_path(r'^room/$', views.RoomListView.as_view(), name='room'),
    re_path(r'^room/(?P<pk>[-\w]+)$', views.RoomDetailView.as_view(), name='room-detail'),
    path(r'^room/create$', views.RoomCreate.as_view(), name='new-room'),
    re_path(r'^room/(?P<pk>[-\w]+)/update$', views.RoomUpdate.as_view(), name='room-update'),
    re_path(r'^room/(?P<pk>[-\w]+)/delete$', views.RoomDelete.as_view(), name='room-delete'),
    #рабочие места
    re_path(r'^workplace/$', views.WorkplaceListView.as_view(), name='workplace'),
    re_path(r'^workplace/(?P<pk>[-\w]+)$', views.WorkplaceDetailView.as_view(), name='workplace-detail'),
    path(r'^workplace/create$', views.WorkplaceCreate.as_view(), name='new-workplace'),
    re_path(r'^workplace/(?P<pk>[-\w]+)/update$', views.WorkplaceUpdate.as_view(), name='workplace-update'),
    re_path(r'^workplace/(?P<pk>[-\w]+)/delete$', views.WorkplaceDelete.as_view(), name='workplace-delete'),
    #сотрудники
    re_path(r'^employee/$', views.EmployeeListView.as_view(), name='employee'),
    re_path(r'^employee/(?P<pk>[-\w]+)$', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path(r'^employee/create$', views.EmployeeCreate.as_view(), name='new-employee'),
    re_path(r'^employee/(?P<pk>[-\w]+)/update$', views.EmployeeUpdate.as_view(), name='employee-update'),
    re_path(r'^employee/(?P<pk>[-\w]+)/delete$', views.EmployeeDelete.as_view(), name='employee-delete'),
    #Должность
    re_path(r'^post/$', views.postListView.as_view(), name='post'),
    re_path(r'^post/(?P<pk>[-\w]+)$', views.postDetailView.as_view(), name='post-detail'),
    path(r'^post/create$', views.postCreate.as_view(), name='new-post'),
    re_path(r'^post/(?P<pk>[-\w]+)/update$', views.postUpdate.as_view(), name='post-update'),
    re_path(r'^post/(?P<pk>[-\w]+)/delete$', views.postDelete.as_view(), name='post-delete'),
    #Отдел
    re_path(r'^departament/$', views.departamentListView.as_view(), name='departament'),
    re_path(r'^departament/(?P<pk>[-\w]+)$', views.departamentDetailView.as_view(), name='departament-detail'),
    path(r'^departament/create$', views.departamentCreate.as_view(), name='new-departament'),
    re_path(r'^departament/(?P<pk>[-\w]+)/update$', views.departamentUpdate.as_view(), name='departament-update'),
    re_path(r'^departament/(?P<pk>[-\w]+)/delete$', views.departamentDelete.as_view(), name='departament-delete'),
    #софт
    re_path(r'^software/$', views.softwareListView.as_view(), name='software'),
    re_path(r'^software/(?P<pk>[-\w]+)$', views.softwareDetailView.as_view(), name='software-detail'),
    path(r'^software/create$', views.softwareCreate.as_view(), name='new-software'),
    re_path(r'^software/(?P<pk>[-\w]+)/update$', views.softwareUpdate.as_view(), name='software-update'),
    re_path(r'^software/(?P<pk>[-\w]+)/delete$', views.softwareDelete.as_view(), name='software-delete'),
    #ОС
    #рабочие станции
    re_path(r'^workstation/$', views.workstationListView.as_view(), name='workstation'), 
    re_path(r'^workstation/(?P<pk>[-\w]+)$', views.workstationDetailView.as_view(), name='workstation-detail'),
    #принтеры
    re_path(r'^printer/$', views.printerListView.as_view(), name='printer'),
    re_path(r'^printer/(?P<pk>[-\w]+)$', views.printerDetailView.as_view(), name='printer-detail'),
    #ЭЦП
    re_path(r'^digital_signature/$', views.digitalSignatureListView.as_view(), name='digital-signature'),
    #Производитель
    
    re_path(r'^manufacturer/$', views.manufacturerListView.as_view(), name='manufacturer'),
    re_path(r'^manufacturer/(?P<pk>[-\w]+)$', views.manufacturerDetailView.as_view(), name='manufacturer-detail'),
    path(r'^manufacturer/create$', views.manufacturerCreate.as_view(), name='new-manufacturer'),
    re_path(r'^manufacturer/(?P<pk>[-\w]+)/update$', views.manufacturerUpdate.as_view(), name='manufacturer-update'),
    re_path(r'^manufacturer/(?P<pk>[-\w]+)/delete$', views.manufacturerDelete.as_view(), name='manufacturer-delete'),
]