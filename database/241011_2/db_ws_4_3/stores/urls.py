from django.urls import path
from . import views

app_name = 'stores'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:store_pk>/', views.detail, name='detail'),
    path('create_store/', views.create_store, name='create_store'),
    path('<int:store_pk>/add_product/', views.add_product, name='add_product'),
]
