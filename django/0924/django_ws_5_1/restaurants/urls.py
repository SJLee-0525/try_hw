from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'restaurants'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]
