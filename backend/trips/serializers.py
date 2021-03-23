from rest_framework import serializers
from .models import Trip


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('start', 'end', 'date', 'distance')


class TripDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
