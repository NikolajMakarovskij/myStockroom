""" URL Configuration

"""
from django.contrib import admin
from django.urls import include
from django.urls import path 

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    
]

urlpatterns += [  
    path('counterparty/', include(('counterparty.urls','counterparty'), namespace='counterparty'), ),
    path('signature/', include(('signature.urls','signature'), namespace='signature'), ),
    path('ups/', include(('ups.urls','ups'), namespace='ups'), ),
    path('printer/', include(('printer.urls','printer'), namespace='printer'), ),
    path('consumables/', include(('consumables.urls','consumables'), namespace='consumables'), ),
    path('workstation/', include(('workstation.urls','workstation'), namespace='workstation'), ),
    path('software/', include(('software.urls','software'), namespace='software'), ),
    path('employee/', include(('employee.urls','employee'), namespace='employee'), ),
    path('workplace/', include(('workplace.urls','workplace'), namespace='workplace'), ),
    path('', include('catalog.urls')),
    
    path('accounts/', include('django.contrib.auth.urls')),
] 

