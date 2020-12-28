from django.db import models

# Create your models here.

class MoodBlock(models.Model):
    track = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    audio = models.CharField(max_length=200)