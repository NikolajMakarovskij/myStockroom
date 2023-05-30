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
    re_path(r'^monitor/$', monitorListView.as_view(), name='monitor_list'),
    re_path(r'^monitor/search$', monitorListView.as_view(), name='monitor_search'), 
    re_path(r'^monitor/(?P<pk>[-\w]+)$', monitorDetailView.as_view(), name='monitor-detail'),
    path(r'^monitor/create$', monitorCreate.as_view(), name='new-monitor'),
    re_path(r'^monitor/(?P<pk>[-\w]+)/update$', monitorUpdate.as_view(), name='monitor-update'),
    re_path(r'^monitor/(?P<pk>[-\w]+)/delete$', monitorDelete.as_view(), name='monitor-delete'),
    #Клавиатура
    re_path(r'^keyBoard/$', keyBoardListView.as_view(), name='keyBoard_list'),
    re_path(r'^keyBoard/search$', keyBoardListView.as_view(), name='keyBoard_search'), 
    re_path(r'^keyBoard/(?P<pk>[-\w]+)$', keyBoardDetailView.as_view(), name='keyBoard-detail'),
    path(r'^keyBoard/create$', keyBoardCreate.as_view(), name='new-keyBoard'),
    re_path(r'^keyBoard/(?P<pk>[-\w]+)/update$', keyBoardUpdate.as_view(), name='keyBoard-update'),
    re_path(r'^keyBoard/(?P<pk>[-\w]+)/delete$', keyBoardDelete.as_view(), name='keyBoard-delete'),
    #мышь
    re_path(r'^mouse/$', mouseListView.as_view(), name='mouse_list'), 
    re_path(r'^mouse/search$', mouseListView.as_view(), name='mouse_search'),
    re_path(r'^mouse/(?P<pk>[-\w]+)$', mouseDetailView.as_view(), name='mouse-detail'),
    path(r'^mouse/create$', mouseCreate.as_view(), name='new-mouse'),
    re_path(r'^mouse/(?P<pk>[-\w]+)/update$', mouseUpdate.as_view(), name='mouse-update'),
    re_path(r'^mouse/(?P<pk>[-\w]+)/delete$', mouseDelete.as_view(), name='mouse-delete'),
]