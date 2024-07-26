from django.urls import include, path, re_path

from .routers import router
from .views import (
    AccountingCategoriesView, AccountingCreate, AccountingDelete, AccountingDetailView,
    AccountingIndexView, AccountingUpdate, AccountingView, CategoryCreate,
    CategoryDelete, CategoryUpdate, CategoryView,)

urlpatterns = [
    re_path('api/v1/', include(router.urls)),
    path('', AccountingIndexView.as_view(), name='accounting_index'),
    # accounting
    path('accounting/', AccountingView.as_view(), name='accounting_list'),
    path('accounting/search', AccountingView.as_view(), name='accounting_search'),
    path('accounting/category/<slug:category_slug>', AccountingCategoriesView.as_view(), name='category'),
    re_path(r'^accounting/(?P<pk>[-\w]+)$', AccountingDetailView.as_view(), name='accounting-detail'),
    re_path(r'^accounting/create/$', AccountingCreate.as_view(), name='new-accounting'),
    re_path(r'^accounting/(?P<pk>[-\w]+)/update$', AccountingUpdate.as_view(), name='accounting-update'),
    re_path(r'^accounting/(?P<pk>[-\w]+)/delete$', AccountingDelete.as_view(), name='accounting-delete'),
    # categories
    path('categories/', CategoryView.as_view(), name='categories_list'),
    path('categories/search', CategoryView.as_view(), name='categories_search'),
    re_path(r'^categories/create/$', CategoryCreate.as_view(), name='new-categories'),
    re_path(r'^categories/(?P<pk>[-\w]+)/update$', CategoryUpdate.as_view(), name='categories-update'),
    re_path(r'^categories/(?P<pk>[-\w]+)/delete$', CategoryDelete.as_view(), name='categories-delete'),
    ]
