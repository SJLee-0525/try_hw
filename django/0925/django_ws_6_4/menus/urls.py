from django.urls import path
from . import views


app_name = 'menus'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:menu_pk>/', views.detail, name='detail'),
    # path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    # path('<int:menu_pk>/edit/', views.edit, name='edit'),
    path('<int:menu_pk>/update/', views.update, name='update'),
    path('<int:menu_pk>/delete/', views.delete, name='delete'),
]