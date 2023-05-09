from django.db import models


# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    image_link = models.CharField(max_length=30)
    facebook_link = models.CharField(max_length=30)
    # genres = models.CharField(max_length=30)
    website = models.CharField(max_length=30)
    seeking_talent = models.BooleanField()
    seeking_description = models.CharField(max_length=30)


class Artist(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    image_link = models.CharField(max_length=30)
    facebook_link = models.CharField(max_length=30)
    # genres = models.CharField(max_length=30)
    website = models.CharField(max_length=30)
    seeking_venue = models.BooleanField()
    seeking_description = models.CharField(max_length=30)