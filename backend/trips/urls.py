from django.urls import path
from .views import AddTripView


urlpatterns = [
    path('trip/add/', AddTripView, name="add-trip"),
]
