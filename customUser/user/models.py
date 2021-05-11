from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    Roles = (
        ('A', 'Agent'),
        ('O', 'Office'),
    )
    role = models.CharField(max_length=1, choices=Roles)
