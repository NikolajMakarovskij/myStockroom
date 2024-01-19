from django.urls import path
from .views import IndexView, UserView, UserRegister, UserLogin, UserLogout

urlpatterns = [
    # главная
    path('', IndexView.as_view(), name='index'),
    path('api/register/', UserRegister.as_view(), name='register'),
    path('api/login/', UserLogin.as_view(), name='login'),
    path('api/logout/', UserLogout.as_view(), name='logout'),
    path('api/user/', UserView.as_view(), name='user'),

]
