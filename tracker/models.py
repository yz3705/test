from django.db import models

# Create your models here.

class Squirrel(models.Model):
    latitude = models.FloatField(blank=False)
    longitude = models.FloatField(blank=False)
    unique_squirrel_id = models.CharField(max_length=14)
    shift = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    age = models.CharField(max_length = 200)
    primary_fur_color = models.CharField(max_length = 200)
    location = models.CharField(max_length = 200)
    specific_location = models.CharField(max_length = 200)
    running = models.BooleanField()
    chasing = models.BooleanField()
    climbing = models.BooleanField()
    eating = models.BooleanField()
    foraging = models.BooleanField()
    other_activities = models.CharField(max_length = 200)
    kuks = models.BooleanField()
    quaas = models.BooleanField()
    moans = models.BooleanField()
    tail_flags = models.BooleanField()
    tail_twitches = models.BooleanField()
    approaches = models.BooleanField()
    indifferent = models.BooleanField()
    runs_from = models.BooleanField()
