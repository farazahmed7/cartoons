from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Cartoon(models.Model):
    photo_link=models.CharField(max_length=1000)
    name=models.CharField(max_length=1000)
    def __str__(self):
        return self.name

class Season(models.Model):
    cartoon=models.ForeignKey(Cartoon)
    season_name=models.CharField(max_length=500)
    def __str__(self):
        return (self.cartoon.name+ " " +self.season_name)


class Episode(models.Model):
    cartoon=models.ForeignKey(Cartoon)
    season=models.ForeignKey(Season)
    episode_name=models.CharField(max_length=500)
    episode_link=models.CharField(max_length=1000)
    def __str__(self):
        return self.episode_name



class RequestCartoon(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

