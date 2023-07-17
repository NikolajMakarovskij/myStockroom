from django.urls import path, re_path
from .views import (
                    DecommissionView, DecomCategoriesView, HistoryDecView, HistoryDecCategoriesView,
                    DisposalView, DispCategoriesView, HistoryDisView, HistoryDisCategoriesView
                    )

urlpatterns = [

    # Decommission
    path('decom/', DecommissionView.as_view(), name='decom_list'),
    path('decom/search', DecommissionView.as_view(), name='decom_search'),
    path('decom/category/<slug:category_slug>', DecomCategoriesView.as_view(), name='decom_category'),

    #path('devices/stockroom/add/<uuid:device_id>/', stock_add_device, name='stock_add_device'),
    #path('devices/stockroom/remove/<uuid:devices_id>/', stock_remove_device, name='stock_remove_device'),


    path('decom/history/', HistoryDecView.as_view(), name='history_dec_list'),
    path('decom/history/search', HistoryDecView.as_view(), name='history_decom_search'),
    path('decom/history/category/<slug:category_slug>', HistoryDecCategoriesView.as_view(),
         name='history_dec_category'),
    #path('devices/stockroom/move/<uuid:device_id>/', move_device_from_stock, name='move_device'),

    # Disposal
    path('disposal/', DisposalView.as_view(), name='disp_list'),
    path('disposal/search', DisposalView.as_view(), name='disp_search'),
    path('disposal/category/<slug:category_slug>', DispCategoriesView.as_view(), name='disp_category'),

    # path('devices/stockroom/add/<uuid:device_id>/', stock_add_device, name='stock_add_device'),
    # path('devices/stockroom/remove/<uuid:devices_id>/', stock_remove_device, name='stock_remove_device'),

    path('disposal/history/', HistoryDisView.as_view(), name='history_dis_list'),
    path('disposal/history/search', HistoryDisView.as_view(), name='history_dis_search'),
    path('disposal/history/category/<slug:category_slug>', HistoryDisCategoriesView.as_view(),
         name='history_dis_category'),
    # path('devices/stockroom/move/<uuid:device_id>/', move_device_from_stock, name='move_device'),

]