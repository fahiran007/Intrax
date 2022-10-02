from django.db import models

# Create your models here.
class Creates(models.Model):
    ListingDate = models.CharField(max_length=50)
    writting = models.CharField(max_length=50)
    collage = models.CharField(max_length=50)
class timestamps(models.Model):
    serialNumber = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    fromTime = models.CharField(max_length=50)
    toTime = models.CharField(max_length=50)
    collage = models.CharField(max_length=50)
    writting = models.CharField(max_length=50)
    minutes = models.CharField(max_length=50)