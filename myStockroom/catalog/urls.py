from django.urls import path, re_path, include
from .views import indexView, referencesView

urlpatterns = [
    #главная
    re_path(r'^$', indexView.as_view(), name='index'),
    #справочники
    re_path(r'^references/$', referencesView.as_view(), name='references_list'),
    re_path(r'^references/search$', referencesView.as_view(), name='references_search')

]