from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from datetime import datetime


class Trip(models.Model):
    start = models.CharField(max_length=200)
    end = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now, blank=True)
    distance = models.IntegerField()
    calories = models.IntegerField()

    def __str__(self):
        name = "Trip from " + self.start + " to " + self.end
        return name
