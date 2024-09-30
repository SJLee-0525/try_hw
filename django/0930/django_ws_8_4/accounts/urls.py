from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<int:user_pk>/score/', views.increase_score, name='increase_score'),
    path('<int:user_pk>/myscoreincrease/', views.increase_myscore, name='increase_myscore'),
]
