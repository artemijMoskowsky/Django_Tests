from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    password = models.CharField(max_length=50)
    custom_field = models.CharField(max_length=10)