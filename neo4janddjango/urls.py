from django.conf.urls import url
from neo4janddjango.views import *
from django.urls import path
urlpatterns = [
    path('',personDetails),
    path('getAllPersons',getAllPersons),
    path('city',cityDetails),
    path('getAllCities',getAllCities),
    path('connectPaC',connectPaC),
    path('connectPaP',connectPaP)
]