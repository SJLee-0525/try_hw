from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('follow/<int:author_pk>/', views.follow, name='follow'),
    path('profile/<username>/', views.profile, name='profile'),
]