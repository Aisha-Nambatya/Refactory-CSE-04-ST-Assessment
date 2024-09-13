from django.urls import path
from . import views  

urlpatterns = [
    path('flight_booking/', views.flight_booking, name='flight_booking'),  # URL to access the flight booking form
]
