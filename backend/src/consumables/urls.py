from django.urls import re_path, include
from .routers import router

urlpatterns = [
    re_path("", include(router.urls)),
]
