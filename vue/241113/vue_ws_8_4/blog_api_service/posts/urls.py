from django.urls import path, include
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/', views.category_list_create, name='category_list_create'),
    path('post/', views.post_list_create, name='post_list_create'),
    # path('create_comment/', views.create_comment, name='create_comment'),
]
