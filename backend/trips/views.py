from django.shortcuts import render
from .models import Trip
from .serializers import TripSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET', 'POST'])
def AddTripView(request):
    trips = Trip.objects.all()
    if request.method == 'GET':
        serializer = TripSerializer(trips, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        data = request.data
