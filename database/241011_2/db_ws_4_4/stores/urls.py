from django.urls import path
from . import views


app_name = 'stores'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:store_pk>/', views.detail, name='detail'),
    path('create/', views.stores_create, name='stores_create'),
    path('<int:store_pk>/products_create/', views.products_create, name='products_create'),
    path('<int:store_pk>/delete/<int:product_pk>/delete/', views.delete_product, name='delete_product'),
]
