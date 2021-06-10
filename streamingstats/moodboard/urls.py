from django.urls import path
from . import views

urlpatterns = [
    # /moodboard/
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('callback/', views.callback, name='callback'),
    path('callback/?code=<str:code>', views.callback),
    path('summary/', views.summary, name='summary'),
    path('summary/term=<str:term>/unique=<int:unique>', views.summary),
]