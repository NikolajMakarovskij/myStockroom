from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/v1/auth/', include('rest_framework.urls')),
    path("select2/", include("django_select2.urls")),
    path('admin/', admin.site.urls),

]

urlpatterns += [
    path('decommission/', include(('decommission.urls', 'decommission'), namespace='decommission'), ),
    path('stockroom/', include(('stockroom.urls', 'stockroom'), namespace='stockroom'), ),
    path('counterparty/', include(('counterparty.urls', 'counterparty'), namespace='counterparty'), ),
    path('signature/', include(('signature.urls', 'signature'), namespace='signature'), ),
    path('device/', include(('device.urls', 'device'), namespace='device'), ),
    path('consumables/', include(('consumables.urls', 'consumables'), namespace='consumables'), ),
    path('software/', include(('software.urls', 'software'), namespace='software'), ),
    path('employee/', include(('employee.urls', 'employee'), namespace='employee'), ),
    path('workplace/', include(('workplace.urls', 'workplace'), namespace='workplace'), ),
    path('home/', include(('core.urls', 'core'), namespace='core'), ),


]
