from django.urls import path, include
from . import views

app_name = 'libraries'
urlpatterns = [
    path('', views.index, name='index')
]