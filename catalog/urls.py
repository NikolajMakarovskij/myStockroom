from django.urls import path, re_path
from .views import views

urlpatterns = [
    #главная
    re_path(r'^$', views.indexView.as_view(), name='index'),
    #справочники
    re_path(r'^references/$', views.referencesView.as_view(), name='references'),
    #склад
    re_path(r'^warehouse/$', views.warehouseView.as_view(), name='warehouse'),



    
    #принтеры
    re_path(r'^printer/$', views.printerListView.as_view(), name='printer'),
    re_path(r'^printer/(?P<pk>[-\w]+)$', views.printerDetailView.as_view(), name='printer-detail'),
    path(r'^printer/create$', views.printerCreate.as_view(), name='new-printer'),
    re_path(r'^printer/(?P<pk>[-\w]+)/update$', views.printerUpdate.as_view(), name='printer-update'),
    re_path(r'^printer/(?P<pk>[-\w]+)/delete$', views.printerDelete.as_view(), name='printer-delete'),

    #ЭЦП
    re_path(r'^signature/$', views.signatureListView.as_view(), name='signature'),
    re_path(r'^signature/(?P<pk>[-\w]+)$', views.signatureDetailView.as_view(), name='signature-detail'),
    path(r'^signature/create$', views.signatureCreate.as_view(), name='new-signature'),
    re_path(r'^signature/(?P<pk>[-\w]+)/update$', views.signatureUpdate.as_view(), name='signature-update'),
    re_path(r'^signature/(?P<pk>[-\w]+)/delete$', views.signatureDelete.as_view(), name='signature-delete'),
    #Производитель
    re_path(r'^manufacturer/$', views.manufacturerListView.as_view(), name='manufacturer'),
    re_path(r'^manufacturer/(?P<pk>[-\w]+)$', views.manufacturerDetailView.as_view(), name='manufacturer-detail'),
    path(r'^manufacturer/create$', views.manufacturerCreate.as_view(), name='new-manufacturer'),
    re_path(r'^manufacturer/(?P<pk>[-\w]+)/update$', views.manufacturerUpdate.as_view(), name='manufacturer-update'),
    re_path(r'^manufacturer/(?P<pk>[-\w]+)/delete$', views.manufacturerDelete.as_view(), name='manufacturer-delete'),
    #Накопитель
    re_path(r'^storage/$', views.storageListView.as_view(), name='storage'),
    re_path(r'^storage/(?P<pk>[-\w]+)$', views.storageDetailView.as_view(), name='storage-detail'),
    path(r'^storage/create$', views.storageCreate.as_view(), name='new-storage'),
    re_path(r'^storage/(?P<pk>[-\w]+)/update$', views.storageUpdate.as_view(), name='storage-update'),
    re_path(r'^storage/(?P<pk>[-\w]+)/delete$', views.storageDelete.as_view(), name='storage-delete'),
    #ИБП
    re_path(r'^ups/$', views.upsListView.as_view(), name='ups'),
    re_path(r'^ups/(?P<pk>[-\w]+)$', views.upsDetailView.as_view(), name='ups-detail'),
    path(r'^ups/create$', views.upsCreate.as_view(), name='new-ups'),
    re_path(r'^ups/(?P<pk>[-\w]+)/update$', views.upsUpdate.as_view(), name='ups-update'),
    re_path(r'^ups/(?P<pk>[-\w]+)/delete$', views.upsDelete.as_view(), name='ups-delete'),
    #Кассеты
    re_path(r'^cassette/$', views.cassetteListView.as_view(), name='cassette'),
    re_path(r'^cassette/(?P<pk>[-\w]+)$', views.cassetteDetailView.as_view(), name='cassette-detail'),
    path(r'^cassette/create$', views.cassetteCreate.as_view(), name='new-cassette'),
    re_path(r'^cassette/(?P<pk>[-\w]+)/update$', views.cassetteUpdate.as_view(), name='cassette-update'),
    re_path(r'^cassette/(?P<pk>[-\w]+)/delete$', views.cassetteDelete.as_view(), name='cassette-delete'),

]