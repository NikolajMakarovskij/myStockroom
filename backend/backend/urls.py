from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("select2/", include("django_select2.urls")),
    path('admin/', admin.site.urls),

]

urlpatterns += [
    path('decommission/', include(('decommission.urls', 'decommission'), namespace='decommission'), ),
    path('stockroom/', include(('stockroom.urls', 'stockroom'), namespace='stockroom'), ),
    path('counterparty/', include(('counterparty.urls', 'counterparty'), namespace='counterparty'), ),
    path('signature/', include(('signature.urls', 'signature'), namespace='signature'), ),
    path('api/device/', include(('device.urls', 'device'), namespace='device'), ),
    path('consumables/', include(('consumables.urls', 'consumables'), namespace='consumables'), ),
    path('accounting/', include(('accounting.urls', 'accounting'), namespace='accounting'), ),
    path('software/', include(('software.urls', 'software'), namespace='software'), ),
    path('employee/', include(('employee.urls', 'employee'), namespace='employee'), ),
    path('workplace/', include(('workplace.urls', 'workplace'), namespace='workplace'), ),
    path('home/', include(('core.urls', 'core'), namespace='core'), ),


]
