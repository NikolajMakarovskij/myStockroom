from django.urls import path
from .views import IndexView

urlpatterns = [
    # главная
    path('', IndexView.as_view(), name='index'),

]
