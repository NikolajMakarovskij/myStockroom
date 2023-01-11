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
    path('employee/', include(('employee.urls','employee'), namespace='employee'), ),
    path('workplace/', include(('workplace.urls','workplace'), namespace='workplace'), ),
    path('', include('catalog.urls')),
    
    path('accounts/', include('django.contrib.auth.urls')),
] 

