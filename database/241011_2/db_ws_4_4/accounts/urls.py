from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('update_user/', views.update_user, name='update_user'),
]