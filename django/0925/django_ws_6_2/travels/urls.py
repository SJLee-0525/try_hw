from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'travels'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
]
