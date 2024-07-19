# mobile/models.py

from django.db import models

class Mobile(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    RAM = models.CharField(max_length=100)
    ROM = models.CharField(max_length=100)
    battery = models.CharField(max_length=100)
    OS = models.CharField(max_length=100)
    network = models.CharField(max_length=100)
    primary_cam = models.CharField(max_length=100)
    secondary_cam = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    quantity = models.IntegerField()
