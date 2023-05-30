from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from myBlog.forms import *
from tandegna.models import *
from django.contrib import messages





# Create your views here.
# def sendMail(request):
 #   send_mail(subject = 'That’s your subject', message = 'Message envoyer',  from_email = 'paul.mandraitsara@advalorem-solutions.com', recipient_list = ['vstylepaul@gmail.com',], auth_user = 'manda', auth_password = 'manda',fail_silently = False,)
  #  return HttpResponse("thanks")


    # send_mail('Subject here', 'Here is the message.', 'paul.mandraitsara@advalorem-solutions.com', ['paul.mandraitsara@advalorem-solutions.com'], fail_silently=False)


def sendMail(request,email,id):
        super = User.objects.get(email=email,id=id)    
        print(super.email)     

          # create a variable to keep track of the form
        messageSent = False

        # check if form has been submitted
        if request.method == 'POST':

            form = EmailForm(request.POST)

            # check if data from the form is clean
            if form.is_valid():
                recipient = request.POST['recipient']
                subject = "Email venant de Tandegna"
                message = request.POST['message']

                # send the email to the recipent
                send_mail(subject, message,
                        settings.DEFAULT_FROM_EMAIL,[recipient])
                
                messages.success(request,'email bien envoyé...')
                return redirect('home')
                
                

                

        else:
            form = EmailForm()

        return render(request, 'index_mailaka.html', {

            'form': form,
            'super':super,
        })