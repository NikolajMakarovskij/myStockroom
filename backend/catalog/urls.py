from django.urls import path
from .views import IndexView, ReferencesView

urlpatterns = [
    # главная
    path('', IndexView.as_view(), name='index'),
    # справочники
    path('references/', ReferencesView.as_view(), name='references_list'),
    path('references/search', ReferencesView.as_view(), name='references_search')

]
