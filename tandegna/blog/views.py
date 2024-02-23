
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout #Pour l'auhtentification login ansi Deconnexion
from django.conf import settings
from blog.models import *
from django.contrib import messages
from . import views
from .forms import *
from blog.views import *
from django.http import HttpResponse
from django.core.validators import validate_email # gerer l'erreur d'email
from django.core.exceptions import ValidationError #gerer l'erreur venant d'email

# Create your views here.

#Creation d'une function pour pouvoir y aller à la page d'accueil.

def home(request):
    infoboutique = infoBoutique.objects.first()
    workfloW = workflow.objects.all()
    adresse = infoboutique.adresse
    lot = infoboutique.lot
    mail = infoboutique.mail
    telephone = infoboutique.telephone
    postal = infoboutique.codepostal
    subscribe = subscribModel.objects.all()
    context = {
       'adresse':adresse,
       'lot':lot,
       'mail':mail,
       'telephone':telephone,
       'postal':postal,
       'workflow': workfloW,
       'subscribe':subscribe

    }
    return render(request, 'blog.html', context)

def blogLogout(request):
    logout(request)
    return redirect('home')

def blogLogin(request):    
    infoboutique = infoBoutique.objects.first()
    workfloW = workflow.objects.all()
    
    
    adresse = infoboutique.adresse
    lot = infoboutique.lot
    mail = infoboutique.mail
    telephone = infoboutique.telephone
    postal = infoboutique.codepostal
    loginform = LoginForm(request.POST)
    context = {
       'adresse':adresse,
       'lot':lot,
       'mail':mail,
       'telephone':telephone,
       'postal':postal,
       'workflow': workfloW,
       'logform':loginform,

    }
    if request.method=="POST":
         loginform = LoginForm(request.POST)
       
         if loginform.is_valid():             
             username = request.POST['username']             
             password = request.POST['password']
          
             user = authenticate(username=username,password=password)
             if user is not None:              
                login(request, user)
                id=user.id
                if subscribModel.objects.filter(user_id__exact=id).values():
                    return redirect('home')
                else:
                    return redirect('subscribecomplete')
             else:
                 messages.error(request, "authentification échoué...")
                 for field in loginform.errors:
                     loginform[field].field.widget.attrs['class'] +='is-invalid'
                 return render(request, 'blogLogin.html', context)         
    else:
         return render(request, 'blogLogin.html', context)
    
    return render(request, 'blogLogin.html', context)


def blogInscription(request):
    infoboutique = infoBoutique.objects.first()
    workfloW = workflow.objects.all()    
    adresse = infoboutique.adresse
    lot = infoboutique.lot
    mail = infoboutique.mail
    telephone = infoboutique.telephone
    postal = infoboutique.codepostal
    loginform = SubscribForm()
    context = {
       'adresse':adresse,
       'lot':lot,
       'mail':mail,
       'telephone':telephone,
       'postal':postal,
       'workflow': workfloW,
       'logform':loginform

    }
    if request.method=="POST":
        loginform = SubscribForm(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        try:
            user_exist = User.objects.get(username=username,email=email)
            error = "pseudo ou email déjà existé...."

            messages.error(request, error)
            return render(request, 'blogInscription.html', context)
        except:
            print("exist")
        password = request.POST["password"]
        passwordc = request.POST["passwordc"]
        if password != passwordc:
            messages.error(request, "Mot de passe différent")
            return render(request, 'blogInscription.html', context)
        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, 'L\'email n\'est pas correct')
            return render(request, 'blogInscription.html', context)
        if loginform.is_valid():
            username = request.POST["username"]
            email = request.POST["email"]
            password = request.POST["password"]

            user = User.objects.create_user(username=username, email=email, password=password)

            if user is not None:
                return redirect('blogLogin')
            else:
                messages.error(request, "enregistrement échoué...")
                return render(request, 'blogInscription.html', context)
        else:
            for field in loginform.errors:
               loginform[field].field.widget.attrs['class'] += " is-invalid "
            return render(request, 'blogInscription.html', context)

        
    return render(request, 'blogInscription.html', context)
