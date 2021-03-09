from django.shortcuts import render
from .models import Trip
from .serializers import TripSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.


@api_view(['GET', 'POST'])
def AddTripView(request):
    trips = Trip.objects.all()
    if request.method == 'GET':
        serializer = TripSerializer(trips, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        data = request.data
        serializer = TripSerializer(data=data)
        if serializer.is_Valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
