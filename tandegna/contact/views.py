from django.shortcuts import render,redirect
from blog.models import *
from .forms import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.
def homeContact(request):
    infoboutique = infoBoutique.objects.first()
    workfloW = workflow.objects.all()
    
    adresse = infoboutique.adresse
    lot = infoboutique.lot
    mail = infoboutique.mail
    telephone = infoboutique.telephone
    postal = infoboutique.codepostal
    contactform = contactForm()
    context = {
       'adresse':adresse,
       'lot':lot,
       'mail':mail,
       'telephone':telephone,
       'postal':postal,
       'workflow': workfloW,
       'contactform':contactform

    }
    return render(request, 'contact.html',context)

def sendMail(request):
    contactform = contactForm(request.POST)
    messageSent = False
    context = {
        'contactform':contactform,
    }
    if request.method == 'POST':
        print("request envoyé")
        contactform = contactForm(request.POST)
        if contactform.is_valid():
            recipient = 'pmandraitsara@gmail.com'
            subject = request.POST['objet']
            message = request.POST['message']
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL,[recipient])
            messages.success(request,'email bien envoyé...')
            return redirect('homeContact')
        else:
            messages.error(request,'Erreur survenue...')
            return render(request, 'contact.html')
    return render(request, 'contact.html', context)