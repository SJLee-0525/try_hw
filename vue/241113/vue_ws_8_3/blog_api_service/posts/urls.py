from django.urls import path, include
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/', views.category_list_create, name='category_list_create'),
    # path('create_post/', views.create_post, name='create_post'),
    # path('create_comment/', views.create_comment, name='create_comment'),
]
