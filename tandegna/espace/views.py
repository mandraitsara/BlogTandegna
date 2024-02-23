from django.shortcuts import render,redirect
from blog.models import *
from espace.forms import *

# Create your views here.
def homeEspace(request):
    infoboutique = infoBoutique.objects.first()
    workfloW = workflow.objects.all()
    adresse = infoboutique.adresse
    lot = infoboutique.lot
    mail = infoboutique.mail
    telephone = infoboutique.telephone
    postal = infoboutique.codepostal
   
    subscribeForm = SubscribComplete(request.POST) 
    subscribe = subscribModel.objects.all()
    
    content = {
        'subscribe':subscribe,
        'subscribeForm':subscribeForm,
        'adresse':adresse,
        'lot':lot,
        'mail':mail,
        'telephone':telephone,
        'postal':postal,
        'workflow': workfloW
    }
    return render(request, 'baseEspace/page.html', content)

def subscribecomplete(request):
    subscribeForm = SubscribComplete(request.POST)
    content= {
        'subscribeForm':subscribeForm
    }

    if request.method == 'POST':
        user = request.POST['user']
        type = request.POST['type']
        pack = request.POST['pack']
        phone = request.POST['phone']
        
        if subscribeForm.is_valid():
            subscribe = subscribModel(type=type, pack=pack,phone=phone,user_id=user)
            subscribe.save()            
            return redirect('home')
        else:      
            return render(request, 'subscribeComplete.html', content)
    else:
        return render(request, 'subscribeComplete.html', content)


def superadmin(request):
    templates = 'superadmin.html'
    return render(request,templates)

def clients(request):
    templates = 'clients.html'
    return render(request, templates)

def prestateur(request):
    subscribe = subscribModel.objects.all()
    category = produitCategory.objects.all()
    race = produitRace.objects.all()    
    produitsform = produitsForm()
    

    content = {
        "subscribe":subscribe,
        "produitsform":produitsform,
        "race":race,
        "category":category
    }
    templates = 'prestateur.html'
    return render(request, templates,content)
