from django.db import models

# Create your models here.
class Item(models.Model):
    platform = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    idx = models.CharField(max_length=50)