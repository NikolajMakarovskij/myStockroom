from django.urls import path, re_path, include
from .routers import router
from .views import ConsumableIndexView, ConsumablesView, ConsumablesCategoriesView, ConsumablesDetailView, \
    ConsumablesCreate, ConsumablesUpdate, ConsumablesDelete, AccessoriesView, AccessoriesCategoriesView, \
    AccessoriesDetailView, AccessoriesCreate, AccessoriesUpdate, AccessoriesDelete

urlpatterns = [
    re_path('api/v1/', include(router.urls)),
    path('', ConsumableIndexView.as_view(), name='consumables_index'),
    # Расходники
    path('consumables/', ConsumablesView.as_view(), name='consumables_list'),
    path('consumables/search', ConsumablesView.as_view(), name='consumables_search'),
    path('consumables/category/<slug:category_slug>', ConsumablesCategoriesView.as_view(), name='category'),
    re_path(r'^consumables/(?P<pk>[-\w]+)$', ConsumablesDetailView.as_view(), name='consumables-detail'),
    re_path(r'^consumables/create/$', ConsumablesCreate.as_view(), name='new-consumables'),
    re_path(r'^consumables/(?P<pk>[-\w]+)/update$', ConsumablesUpdate.as_view(), name='consumables-update'),
    re_path(r'^consumables/(?P<pk>[-\w]+)/delete$', ConsumablesDelete.as_view(), name='consumables-delete'),
    # Комплектующие
    path('accessories/', AccessoriesView.as_view(), name='accessories_list'),
    path('accessories/search', AccessoriesView.as_view(), name='accessories_search'),
    path('accessories/category/<slug:category_slug>', AccessoriesCategoriesView.as_view(), name='category_accessories'),
    re_path(r'^accessories/(?P<pk>[-\w]+)$', AccessoriesDetailView.as_view(), name='accessories-detail'),
    re_path(r'^accessories/create/$', AccessoriesCreate.as_view(), name='new-accessories'),
    re_path(r'^accessories/(?P<pk>[-\w]+)/update$', AccessoriesUpdate.as_view(), name='accessories-update'),
    re_path(r'^accessories/(?P<pk>[-\w]+)/delete$', AccessoriesDelete.as_view(), name='accessories-delete'),

]
