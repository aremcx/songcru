from django.db import models
from datetime import datetime

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name



class Song(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date_released = models.DateField()
    likes = models.IntegerField()
    artiste_id = models.IntegerField()

    def __str__(self):
        return self.Artiste


class Lyric(models.Model):
    Song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.TextField()
    song_id = models.IntegerField()


    def __str__(self):
        return self.Song

