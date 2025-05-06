from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("admin/", admin.site.urls),
]

urlpatterns += [
    path(
        "api/decommission/",
        include(("decommission.urls", "decommission"), namespace="decommission"),
    ),
    path(
        "api/stockroom/",
        include(("stockroom.urls", "stockroom"), namespace="stockroom"),
    ),
    path(
        "api/counterparty/",
        include(("counterparty.urls", "counterparty"), namespace="counterparty"),
    ),
    path(
        "signature/",
        include(("signature.urls", "signature"), namespace="signature"),
    ),
    path(
        "api/devices/",
        include(("device.urls", "devices"), namespace="devices"),
    ),
    path(
        "api/consumables/",
        include(("consumables.urls", "consumables"), namespace="consumables"),
    ),
    path(
        "api/accounting/",
        include(("accounting.urls", "accounting"), namespace="accounting"),
    ),
    path(
        "software/",
        include(("software.urls", "software"), namespace="software"),
    ),
    path(
        "api/employee/",
        include(("employee.urls", "employee"), namespace="employee"),
    ),
    path(
        "api/workplace/",
        include(("workplace.urls", "workplace"), namespace="workplace"),
    ),
    path(
        "api/",
        include(("core.urls", "core"), namespace="core"),
    ),
]
