from django.urls import path, re_path
from .views import *

urlpatterns = [  
    #принтеры
    re_path(r'^$', printerListView.as_view(), name='printer_list'),
    re_path(r'^search$', printerListView.as_view(), name='printer_search'),
    path('category/<slug:category_slug>', printerCategoryListView.as_view(), name='category'),
    re_path(r'^(?P<pk>[-\w]+)$', printerDetailView.as_view(), name='printer-detail'),
    path(r'^create$', printerCreate.as_view(), name='new-printer'),
    re_path(r'^(?P<pk>[-\w]+)/update$', printerUpdate.as_view(), name='printer-update'),
    re_path(r'^(?P<pk>[-\w]+)/delete$', printerDelete.as_view(), name='printer-delete'),
]