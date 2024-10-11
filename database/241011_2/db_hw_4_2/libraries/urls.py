from . import views
from django.urls import path

app_name = 'libraries'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_pk>/', views.detail, name='detail'),
]