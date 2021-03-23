from django.urls import path
from .views import AddTripView


urlpatterns = [
    path('add/', AddTripView, name="add-trip"),
]
