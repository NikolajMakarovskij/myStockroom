from django.urls import re_path
from .views import IndexView, ReferencesView

urlpatterns = [
    # главная
    re_path(r'^$', IndexView.as_view(), name='index'),
    # справочники
    re_path(r'^references/$', ReferencesView.as_view(), name='references_list'),
    re_path(r'^references/search$', ReferencesView.as_view(), name='references_search')

]
