from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Car(models.Model):
    car = models.CharField(max_length=100)
    prime = models.IntegerField(null=True, blank=True)
    dealership = models.CharField(max_length=100)