from django.shortcuts import render
from .models import Trip
from .serializers import TripSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def AddTripView(request):
    trips = Trip.objects.all()
    if request.method == 'GET':
        serializer = TripSerializer(trips, many=True)
