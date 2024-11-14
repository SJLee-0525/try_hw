from django.urls import path
from . import views


urlpatterns = [
    path('articles/', views.article_list_create),
    path('articles/<int:article_pk>/', views.article_detail),
]