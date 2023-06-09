from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', consumableIndexView.as_view(), name='consumables_index'),
    #Расходники
    path('consumables/', consumablesView.as_view(), name='consumables_list'),
    re_path(r'^consumables/search$', consumablesView.as_view(), name='consumables_search'),
    path('consumables/category/<slug:category_slug>', consumablesCategoriesView.as_view(), name='category'),
    re_path(r'^consumables/(?P<pk>[-\w]+)$', consumablesDetailView.as_view(), name='consumables-detail'),
    path(r'^consumables/create$', consumablesCreate.as_view(), name='new-consumables'),
    re_path(r'^consumables/(?P<pk>[-\w]+)/update$', consumablesUpdate.as_view(), name='consumables-update'),
    re_path(r'^consumables/(?P<pk>[-\w]+)/delete$', consumablesDelete.as_view(), name='consumables-delete'),
    #Комплектующие
    path('accessories/', accessoriesView.as_view(), name='accessories_list'),
    re_path(r'^accessories/search$', accessoriesView.as_view(), name='accessories_search'),
    path('accessories/category/<slug:category_slug>', accessoriesCategoriesView.as_view(), name='category_accessories'),
    re_path(r'^accessories/(?P<pk>[-\w]+)$', accessoriesDetailView.as_view(), name='accessories-detail'),
    path(r'^accessories/create$', accessoriesCreate.as_view(), name='new-accessories'),
    re_path(r'^accessories/(?P<pk>[-\w]+)/update$', accessoriesUpdate.as_view(), name='accessories-update'),
    re_path(r'^accessories/(?P<pk>[-\w]+)/delete$', accessoriesDelete.as_view(), name='accessories-delete'),

]