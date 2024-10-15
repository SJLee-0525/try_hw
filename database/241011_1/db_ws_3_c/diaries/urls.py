from django.urls import path
from . import views


app_name = 'diaries'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:diary_pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:diary_pk>/comments/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'),
]