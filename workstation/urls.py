from django.urls import path, re_path
from .views import *

urlpatterns = [
    #рабочие станции
    re_path(r'^$', workstationListView.as_view(), name='workstation_list'),
    re_path(r'^search$', workstationListView.as_view(), name='workstation_search'),  
    path('category/<slug:category_slug>', workstationCategoryListView.as_view(), name='category'),
    re_path(r'^(?P<pk>[-\w]+)$', workstationDetailView.as_view(), name='workstation-detail'),
    path(r'^create$', workstationCreate.as_view(), name='new-workstation'),
    re_path(r'^(?P<pk>[-\w]+)/update$', workstationUpdate.as_view(), name='workstation-update'),
    re_path(r'^(?P<pk>[-\w]+)/delete$', workstationDelete.as_view(), name='workstation-delete'),
    #Монитор
    re_path(r'^monitor/$', monitorListView.as_view(), name='monitor'), 
    re_path(r'^monitor/(?P<pk>[-\w]+)$', monitorDetailView.as_view(), name='monitor-detail'),
    path(r'^monitor/create$', monitorCreate.as_view(), name='new-monitor'),
    re_path(r'^monitor/(?P<pk>[-\w]+)/update$', monitorUpdate.as_view(), name='monitor-update'),
    re_path(r'^monitor/(?P<pk>[-\w]+)/delete$', monitorDelete.as_view(), name='monitor-delete'),
    #Материнская плата
    re_path(r'^motherboard/$', motherboardListView.as_view(), name='motherboard'), 
    re_path(r'^motherboard/(?P<pk>[-\w]+)$', motherboardDetailView.as_view(), name='motherboard-detail'),
    path(r'^motherboard/create$', motherboardCreate.as_view(), name='new-motherboard'),
    re_path(r'^motherboard/(?P<pk>[-\w]+)/update$', motherboardUpdate.as_view(), name='motherboard-update'),
    re_path(r'^motherboard/(?P<pk>[-\w]+)/delete$', motherboardDelete.as_view(), name='motherboard-delete'),
    #Процессор
    re_path(r'^cpu/$', cpuListView.as_view(), name='cpu'), 
    re_path(r'^cpu/(?P<pk>[-\w]+)$', cpuDetailView.as_view(), name='cpu-detail'),
    path(r'^cpu/create$', cpuCreate.as_view(), name='new-cpu'),
    re_path(r'^cpu/(?P<pk>[-\w]+)/update$', cpuUpdate.as_view(), name='cpu-update'),
    re_path(r'^cpu/(?P<pk>[-\w]+)/delete$', cpuDelete.as_view(), name='cpu-delete'),
    #Видеокарта
    re_path(r'^gpu/$', gpuListView.as_view(), name='gpu'), 
    re_path(r'^gpu/(?P<pk>[-\w]+)$', gpuDetailView.as_view(), name='gpu-detail'),
    path(r'^gpu/create$', gpuCreate.as_view(), name='new-gpu'),
    re_path(r'^gpu/(?P<pk>[-\w]+)/update$', gpuUpdate.as_view(), name='gpu-update'),
    re_path(r'^gpu/(?P<pk>[-\w]+)/delete$', gpuDelete.as_view(), name='gpu-delete'),
    #оперативная память
    re_path(r'^ram/$', ramListView.as_view(), name='ram'), 
    re_path(r'^ram/(?P<pk>[-\w]+)$', ramDetailView.as_view(), name='ram-detail'),
    path(r'^ram/create$', ramCreate.as_view(), name='new-ram'),
    re_path(r'^ram/(?P<pk>[-\w]+)/update$', ramUpdate.as_view(), name='ram-update'),
    re_path(r'^ram/(?P<pk>[-\w]+)/delete$', ramDelete.as_view(), name='ram-delete'),
    #SSD
    re_path(r'^ssd/$', ssdListView.as_view(), name='ssd'), 
    re_path(r'^ssd/(?P<pk>[-\w]+)$', ssdDetailView.as_view(), name='ssd-detail'),
    path(r'^ssd/create$', ssdCreate.as_view(), name='new-ssd'),
    re_path(r'^ssd/(?P<pk>[-\w]+)/update$', ssdUpdate.as_view(), name='ssd-update'),
    re_path(r'^ssd/(?P<pk>[-\w]+)/delete$', ssdDelete.as_view(), name='ssd-delete'),
    #HDD
    re_path(r'^hdd/$', hddListView.as_view(), name='hdd'), 
    re_path(r'^hdd/(?P<pk>[-\w]+)$', hddDetailView.as_view(), name='hdd-detail'),
    path(r'^hdd/create$', hddCreate.as_view(), name='new-hdd'),
    re_path(r'^hdd/(?P<pk>[-\w]+)/update$', hddUpdate.as_view(), name='hdd-update'),
    re_path(r'^hdd/(?P<pk>[-\w]+)/delete$', hddDelete.as_view(), name='hdd-delete'),
    #Блок питания
    re_path(r'^dcpower/$', dcpowerListView.as_view(), name='dcpower'), 
    re_path(r'^dcpower/(?P<pk>[-\w]+)$', dcpowerDetailView.as_view(), name='dcpower-detail'),
    path(r'^dcpower/create$', dcpowerCreate.as_view(), name='new-dcpower'),
    re_path(r'^dcpower/(?P<pk>[-\w]+)/update$', dcpowerUpdate.as_view(), name='dcpower-update'),
    re_path(r'^dcpower/(?P<pk>[-\w]+)/delete$', dcpowerDelete.as_view(), name='dcpower-delete'),
    #Клавиатура
    re_path(r'^keyBoard/$', keyBoardListView.as_view(), name='keyBoard'), 
    re_path(r'^keyBoard/(?P<pk>[-\w]+)$', keyBoardDetailView.as_view(), name='keyBoard-detail'),
    path(r'^keyBoard/create$', keyBoardCreate.as_view(), name='new-keyBoard'),
    re_path(r'^keyBoard/(?P<pk>[-\w]+)/update$', keyBoardUpdate.as_view(), name='keyBoard-update'),
    re_path(r'^keyBoard/(?P<pk>[-\w]+)/delete$', keyBoardDelete.as_view(), name='keyBoard-delete'),
    #мышь
    re_path(r'^mouse/$', mouseListView.as_view(), name='mouse'), 
    re_path(r'^mouse/(?P<pk>[-\w]+)$', mouseDetailView.as_view(), name='mouse-detail'),
    path(r'^mouse/create$', mouseCreate.as_view(), name='new-mouse'),
    re_path(r'^mouse/(?P<pk>[-\w]+)/update$', mouseUpdate.as_view(), name='mouse-update'),
    re_path(r'^mouse/(?P<pk>[-\w]+)/delete$', mouseDelete.as_view(), name='mouse-delete'),
]