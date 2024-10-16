from django.urls import path, include
from . import views

urlpatterns = [
    path('artists/', views.artists_list),
]
