from django.urls import path
from .views import IndexView, SessionView, WhoAmIView, get_csrf, login_view, logout_view

urlpatterns = [
    # главная
    path("home/", IndexView.as_view(), name="index"),
    path("csrf/", get_csrf, name="api-csrf"),
    path("login/", login_view, name="api-login"),
    path("logout/", logout_view, name="api-logout"),
    path("session/", SessionView.as_view(), name="api-session"),  # new
    path("whoami/", WhoAmIView.as_view(), name="api-whoami"),  # new
]
