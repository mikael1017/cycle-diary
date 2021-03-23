from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from datetime import datetime


class Trip(models.Model):
    class TripType(models.TextChoices):
        ROUND_TRIP = 'Roundtrip'
        ONEWAY_TRIP = 'One way'

    start = models.CharField(max_length=200)
    end = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now, blank=True)
    distance = models.IntegerField()
    power = models.IntegerField(default=0)
    calories = models.IntegerField()
    time = models.IntegerField(default=0)
    trip_type = models.CharField(
        max_length=50, choices=TripType.choices, default=TripType.ROUND_TRIP)

    def __str__(self):
        name = "Trip from " + self.start + " to " + self.end
        return name
