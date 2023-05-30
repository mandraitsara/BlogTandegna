from django.urls import path
from mailaka.views import *

urlpatterns = [
    path('mailaka/<str:email><int:id>', sendMail, name="sendMail"),
]
