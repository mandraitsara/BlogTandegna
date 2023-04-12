from django.urls import path
from conversation.views import *

urlpatterns = [
    path('conversation/<int:user_id>',conversation, name="conversation")
]