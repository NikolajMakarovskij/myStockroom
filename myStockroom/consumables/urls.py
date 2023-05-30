from django.urls import path, re_path
from .views import *

urlpatterns = [
    #Расходники
    path('', consumablesView.as_view(), name='consumables_list'),
    re_path(r'^search$', consumablesView.as_view(), name='consumables_search'),
    path('category/<slug:category_slug>', consumablesCategoriesView.as_view(), name='category'),
    re_path(r'^(?P<pk>[-\w]+)$', consumablesDetailView.as_view(), name='consumables-detail'),
    path(r'^create$', consumablesCreate.as_view(), name='new-consumables'),
    re_path(r'^(?P<pk>[-\w]+)/update$', consumablesUpdate.as_view(), name='consumables-update'),
    re_path(r'^(?P<pk>[-\w]+)/delete$', consumablesDelete.as_view(), name='consumables-delete'),

]