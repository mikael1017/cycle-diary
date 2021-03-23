from django.shortcuts import render
from .models import Trip
from .serializers import TripSerializer, TripDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import datetime, timezone, timedelta

# Create your views here.


@api_view(['GET', 'POST'])
def AddTripView(request):
    queryset = Trip.objects.all()
    if request.method == 'GET':
        serializer = TripDetailSerializer(queryset, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        data = request.data
        serializer = TripDetailSerializer(data=data)
        if serializer.is_Valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def TripBasicView(request):
    queryset = Trip.objects.all()
    serializer = TripSerializer
    return Response(serializer.data)
