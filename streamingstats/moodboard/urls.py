from django.urls import path
from . import views

urlpatterns = [
    # /moodboard/
    path('', views.index, name='index'),
    path('term=<str:term>', views.index),
]