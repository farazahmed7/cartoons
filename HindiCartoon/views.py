from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from HindiCartoon.models import Cartoon, Season
from rest_framework.response import Response
from HindiCartoon.serializer import CartoonsSerializer, EpisodesSerializer, SeasonsSerializer


@csrf_exempt
@api_view(['GET', 'POST', ])
def cartoonList(request):
    if request.method=="POST":
        cartoons=Cartoon.objects.all()
        ser=CartoonsSerializer(cartoons,many=True)
        return Response(ser.data)
    return HttpResponse("Asd")

@csrf_exempt
@api_view(['GET', 'POST', ])
def seasonList(request):
    if request.method=="POST":
        cartoonName=str(request.POST['cartoon_name'])
        cartoon=Cartoon.objects.get(name=cartoonName)
        list=cartoon.season_set.all()
        ser=SeasonsSerializer(list,many=True)
        return Response(ser.data)
    return HttpResponse("ASda")


@csrf_exempt
@api_view(['GET', 'POST', ])
def episodeList(request):
    if request.method=="POST":
        cartoon_name=str(request.POST['cartoon_name'])
        season_name=str(request.POST['season_name'])
        cartoon=Cartoon.objects.get(name=cartoon_name)
        seasonName=Season.objects.filter(cartoon=cartoon)
        a=seasonName.get(season_name=season_name)
        list= a.episode_set.all()
        ser=EpisodesSerializer(list,many=True)
        return Response(ser.data)
    return HttpResponse("ASda")
