from django.urls import path
from . import views

urlpatterns = [
    path('locations/', views.location_list),
    path('locations/<int:location_pk>/stations/', views.create_station),
    path('stations/', views.station_list),
    path('stations/<int:station_pk>/', views.station_detail),
]