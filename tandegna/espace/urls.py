from django.urls import path, include
from .views import *

urlpatterns = [
    path('', homeEspace , name="homeespace"),
    path('complete/', subscribecomplete, name="subscribecomplete"),
    path('superadmin/', superadmin, name='superadmin'),
    path('clients/', clients, name='clients'),
    path('prestateur/', prestateur, name='prestateur'),

]
