from django.shortcuts import render
from tandegna.models import *

# Create your views here.
def conversation(request,user_id):
    user = User.objects.get(username=user_id)
    return render(request, 'conversation/index.html',{'user':user})