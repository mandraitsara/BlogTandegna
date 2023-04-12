from django.urls import path
from mailaka.views import *

urlpatterns = [
    path('mailaka/', sendMail, name="sendMail"),
]
