from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Cartoon(models.Model):
    photo_link=models.CharField(max_length=1000)
    name=models.CharField(max_length=1000)
    def __str__(self):
        return self.name


class Episode(models.Model):
    cartoon=models.ForeignKey(Cartoon)
    episode_name=models.CharField(max_length=500)
    episode_link=models.CharField(max_length=1000)
    def __str__(self):
        return self.episode_name