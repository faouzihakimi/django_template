# home/models.py
from django.db import models

from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(Group, related_name='home_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='home_user_permissions')
# Create your models here.

class CO2(models.Model):
    date = models.DateField()
    average = models.FloatField()

    class   Meta:
        ordering = ('date',)