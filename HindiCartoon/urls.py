__author__ = 'abc'


from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/cartoons$', views.cartoonList, name='list'),
    url(r'^api/episodes$', views.episodeList, name='list'),




]