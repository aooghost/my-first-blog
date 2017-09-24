from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genere = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)
    price = models.CharField(max_length=20)

    description = models.CharField(max_length=1000, default="no data", null=True)
    sensitivity = models.CharField(max_length=20, default="no data")
    frequency = models.CharField(max_length=20, default="no data")
    impedance = models.CharField(max_length=20, default="no data")
    cable = models.CharField(max_length=50, default="no data")
    noise = models.CharField(max_length=40, default="no data")

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)

    def __str__(self):
        return self.song_title
