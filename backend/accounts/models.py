from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionMixin, BaseUserManager

class UserAccount(AbstractBaseUser, PermissionsMixin):
    """Database models for the users"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()