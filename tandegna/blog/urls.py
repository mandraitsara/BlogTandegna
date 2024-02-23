
from django.urls import path
from blog.views import *



urlpatterns = [
    path('', home, name="home"),
    path('blogLogin/', blogLogin, name="blogLogin"),
    # path('blogLogin/', subscribcomplte, name="subscribcomplte"),
    path('blogInscription/', blogInscription, name="blogInscription"),
    path('blogLogout/',blogLogout,name="blogLogout"),]

# pour prestateur : presta
# staP/.14
