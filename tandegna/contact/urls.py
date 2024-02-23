from django.urls import path
from contact.views import *



urlpatterns = [
    path('', homeContact, name="homeContact"),
    path('mail', sendMail, name="sendmail"),
    
]
