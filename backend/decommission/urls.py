from django.urls import path, re_path
from .views import (
                    DecommissionView, DecomCategoriesView, HistoryDecView, HistoryDecCategoriesView,
                    DisposalView, DispCategoriesView, HistoryDisView, HistoryDisCategoriesView,
                    add_decommission, remove_decommission, add_disposal, remove_disposal
                    )

urlpatterns = [

    # Decommission
    path('decom/', DecommissionView.as_view(), name='decom_list'),
    path('decom/search', DecommissionView.as_view(), name='decom_search'),
    path('decom/category/<slug:category_slug>', DecomCategoriesView.as_view(), name='decom_category'),

    path('decom/add/<uuid:device_id>/', add_decommission, name='add_decom'),
    path('decom/remove/<uuid:devices_id>/', remove_decommission, name='remove_decom'),


    path('decom/history/', HistoryDecView.as_view(), name='history_dec_list'),
    path('decom/history/search', HistoryDecView.as_view(), name='history_decom_search'),
    path('decom/history/category/<slug:category_slug>', HistoryDecCategoriesView.as_view(),
         name='history_dec_category'),

    # Disposal
    path('disposal/', DisposalView.as_view(), name='disp_list'),
    path('disposal/search', DisposalView.as_view(), name='disp_search'),
    path('disposal/category/<slug:category_slug>', DispCategoriesView.as_view(), name='disp_category'),

    path('disposal/add/<uuid:devices_id>/', add_disposal, name='add_disp'),
    path('disposal/remove/<uuid:devices_id>/', remove_disposal, name='remove_disp'),

    path('disposal/history/', HistoryDisView.as_view(), name='history_dis_list'),
    path('disposal/history/search', HistoryDisView.as_view(), name='history_dis_search'),
    path('disposal/history/category/<slug:category_slug>', HistoryDisCategoriesView.as_view(),
         name='history_dis_category'),

]
