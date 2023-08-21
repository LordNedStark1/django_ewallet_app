from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    phoneNumber = models.CharField(max_length=11)
    first_name = models.CharField(max_length=150, default=None)
    last_name = models.CharField(max_length=150, default=None)
