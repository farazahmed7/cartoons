__author__ = 'abc'
from .models import Cartoon,Episode
from rest_framework import serializers

class CartoonsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cartoon
        fields=('name','photo_link')

class EpisodesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Episode
        fields=('episode_name','episode_link')