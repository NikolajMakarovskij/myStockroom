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
    re_path(r'^OS/$', views.OSListView.as_view(), name='OS'),
    re_path(r'^OS/(?P<pk>[-\w]+)$', views.OSDetailView.as_view(), name='OS-detail'),
    path(r'^OS/create$', views.OSCreate.as_view(), name='new-OS'),
    re_path(r'^OS/(?P<pk>[-\w]+)/update$', views.OSUpdate.as_view(), name='OS-update'),
    re_path(r'^OS/(?P<pk>[-\w]+)/delete$', views.OSDelete.as_view(), name='OS-delete'),
    #рабочие станции
    re_path(r'^workstation/$', views.workstationListView.as_view(), name='workstation'), 
    re_path(r'^workstation/(?P<pk>[-\w]+)$', views.workstationDetailView.as_view(), name='workstation-detail'),
    path(r'^workstation/create$', views.workstationCreate.as_view(), name='new-workstation'),
    re_path(r'^workstation/(?P<pk>[-\w]+)/update$', views.workstationUpdate.as_view(), name='workstation-update'),
    re_path(r'^workstation/(?P<pk>[-\w]+)/delete$', views.workstationDelete.as_view(), name='workstation-delete'),
    #Монитор
    re_path(r'^monitor/$', views.monitorListView.as_view(), name='monitor'), 
    re_path(r'^monitor/(?P<pk>[-\w]+)$', views.monitorDetailView.as_view(), name='monitor-detail'),
    path(r'^monitor/create$', views.monitorCreate.as_view(), name='new-monitor'),
    re_path(r'^monitor/(?P<pk>[-\w]+)/update$', views.monitorUpdate.as_view(), name='monitor-update'),
    re_path(r'^monitor/(?P<pk>[-\w]+)/delete$', views.monitorDelete.as_view(), name='monitor-delete'),
    #Материнская плата
    re_path(r'^motherboard/$', views.motherboardListView.as_view(), name='motherboard'), 
    re_path(r'^motherboard/(?P<pk>[-\w]+)$', views.motherboardDetailView.as_view(), name='motherboard-detail'),
    path(r'^motherboard/create$', views.motherboardCreate.as_view(), name='new-motherboard'),
    re_path(r'^motherboard/(?P<pk>[-\w]+)/update$', views.motherboardUpdate.as_view(), name='motherboard-update'),
    re_path(r'^motherboard/(?P<pk>[-\w]+)/delete$', views.motherboardDelete.as_view(), name='motherboard-delete'),

    #принтеры
    re_path(r'^printer/$', views.printerListView.as_view(), name='printer'),
    re_path(r'^printer/(?P<pk>[-\w]+)$', views.printerDetailView.as_view(), name='printer-detail'),
    path(r'^printer/create$', views.printerCreate.as_view(), name='new-printer'),
    re_path(r'^printer/(?P<pk>[-\w]+)/update$', views.printerUpdate.as_view(), name='printer-update'),
    re_path(r'^printer/(?P<pk>[-\w]+)/delete$', views.printerDelete.as_view(), name='printer-delete'),
    #картриджы
    re_path(r'^cartridge/$', views.cartridgeListView.as_view(), name='cartridge'),
    re_path(r'^cartridge/(?P<pk>[-\w]+)$', views.cartridgeDetailView.as_view(), name='cartridge-detail'),
    path(r'^cartridge/create$', views.cartridgeCreate.as_view(), name='new-cartridge'),
    re_path(r'^cartridge/(?P<pk>[-\w]+)/update$', views.cartridgeUpdate.as_view(), name='cartridge-update'),
    re_path(r'^cartridge/(?P<pk>[-\w]+)/delete$', views.cartridgeDelete.as_view(), name='cartridge-delete'),
    #фотовалы
    re_path(r'^fotoval/$', views.fotovalListView.as_view(), name='fotoval'),
    re_path(r'^fotoval/(?P<pk>[-\w]+)$', views.fotovalDetailView.as_view(), name='fotoval-detail'),
    path(r'^fotoval/create$', views.fotovalCreate.as_view(), name='new-fotoval'),
    re_path(r'^fotoval/(?P<pk>[-\w]+)/update$', views.fotovalUpdate.as_view(), name='fotoval-update'),
    re_path(r'^fotoval/(?P<pk>[-\w]+)/delete$', views.fotovalDelete.as_view(), name='fotoval-delete'),
    #Тонеры
    re_path(r'^toner/$', views.tonerListView.as_view(), name='toner'),
    re_path(r'^toner/(?P<pk>[-\w]+)$', views.tonerDetailView.as_view(), name='toner-detail'),
    path(r'^toner/create$', views.tonerCreate.as_view(), name='new-toner'),
    re_path(r'^toner/(?P<pk>[-\w]+)/update$', views.tonerUpdate.as_view(), name='toner-update'),
    re_path(r'^toner/(?P<pk>[-\w]+)/delete$', views.tonerDelete.as_view(), name='toner-delete'),
    #ЭЦП
    re_path(r'^digital_signature/$', views.digitalSignatureListView.as_view(), name='digital-signature'),
    #Производитель
    re_path(r'^manufacturer/$', views.manufacturerListView.as_view(), name='manufacturer'),
    re_path(r'^manufacturer/(?P<pk>[-\w]+)$', views.manufacturerDetailView.as_view(), name='manufacturer-detail'),
    path(r'^manufacturer/create$', views.manufacturerCreate.as_view(), name='new-manufacturer'),
    re_path(r'^manufacturer/(?P<pk>[-\w]+)/update$', views.manufacturerUpdate.as_view(), name='manufacturer-update'),
    re_path(r'^manufacturer/(?P<pk>[-\w]+)/delete$', views.manufacturerDelete.as_view(), name='manufacturer-delete'),
]