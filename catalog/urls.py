from django.urls import path, re_path
from .views import *

urlpatterns = [
    #главная
    re_path(r'^$', indexView.as_view(), name='index'),
    #справочники
    re_path(r'^references/$', referencesView.as_view(), name='references'),



]