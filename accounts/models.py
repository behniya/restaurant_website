from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=150 , blank=True , null=True)
    last_name = models.CharField(max_length=150 , blank=True , null=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)