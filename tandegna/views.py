import time
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login,logout
#from django.views import View
#from django.core.files.storage import FileSystemStorage
from myBlog.forms import *
from tandegna.models import *
#from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from django.core import validators
from django.core.exceptions import ValidationError
from django.core.validators import validate_email



def home(request):
    liste_articles = Article.objects.all()
    
   
   
    form = LoginForm()
    page = request.GET.get('page',1)
    paginator = Paginator(liste_articles, 9)
    #options = Article.objects.get(options='demande')
    image = ArticlePhoto.objects.all()

    try:
        article = paginator.page(page)
    except PageNotAnInteger:
        article = Paginator.page(1)
    except EmptyPage:
        article = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'liste_articles':article,'form':form,'image':image} )
# Create your views here.

def login_tandegna(request):
    if request.method=="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            pwd = request.POST['password']
            user = authenticate(username=username,password=pwd)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Authentification échoué")
                for field in form.errors:
                    form[field].field.widget.attrs['class'] += " is-invalid "
                return render(request, 'login_tandegna.html',{'form':form})
        else:
            for field in form.errors:
               form[field].field.widget.attrs['class'] += " is-invalid "
            return render(request, 'login_tandegna.html',{'form':form})
    else:
        form = LoginForm()
        return render(request, 'login_tandegna.html',{'form':form})

def inscription_tandegna(request):
    form =  InscriptionForm()
    if request.method=="POST":
        form = InscriptionForm(request.POST)
        telephone = request.POST['telephone']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password=  request.POST['password']
        email= request.POST['email']
        passwordC=  request.POST['passwordC']
        check = request.POST['check']

        if check == False:
            messages.error(request, "Tu dois lire et accepter le cochage, s'il te plait...")
            return render(request, "inscription_tandegna.html",{"form":form})

        if len(first_name)<=3:
            messages.error(request, 'Le nom est vraimment court')
            return render(request, 'inscription_tandegna.html',{'form':form})
        
        if len(last_name)<=3:
            messages.error(request, 'Le prenom est vraimment court')
            return render(request, 'inscription_tandegna.html',{'form':form})        
           
        if len(telephone)>10 or len(telephone)<10:
                messages.error(request, 'Le numero telephone n\'est pas bien')
                return render(request, 'inscription_tandegna.html',{'form':form}) 
        
        if passwordC != password:
            messages.error(request, 'Le mot passe ne se correspond pas ...')
            return render(request, 'inscription_tandegna.html',{'form':form}) 

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e, 'L\'email n\'est pas correct')
            return render(request, 'inscription_tandegna.html',{'form':form})   
        
        if form.is_valid():
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            password=  request.POST['password']
            passwordC=  request.POST['passwordC']
            email= request.POST['email']
            telephone = request.POST['telephone']
            
            user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,email=email,telephone=telephone)
            

            
            
            if user is not None:
                return redirect('home')
            else:
                messages.error(request, "Enregistrement échoué...!")
                return render(request, 'inscription_tandegna.html', {'form':form})
        else:
            for field in form.errors:
               form[field].field.widget.attrs['class'] += " is-invalid "
            return render(request, 'inscription_tandegna.html', {'form':form})
    return render(request, 'inscription_tandegna.html', {'form':form})
    
def logout_tandegna(request):
    logout(request)
    return redirect('home')

def myAdmin(request):
    liste_articles = Article.objects.all()
    users = User.objects.all()
    return render(request, 'myAdmin.html',{'liste_articles':liste_articles, 'users':users})

def insertion_du_produit(request):
    form = ArticleForm()

    if request.method=='POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            titre = request.POST['titre']
            race = request.POST['race']
            ages = request.POST['ages']
            description = request.POST['description']
            poids = request.POST['poids']
            options = request.POST['options']
            type = request.POST['type']
            regions = request.POST['regions']
            district = request.POST['district']
            communes = request.POST['communes']
            user_id = request.POST['user_id']
            
            #images = request.POST['images']
            articles = Article(titre=titre,race=race,ages=ages,description=description,poids=poids,options=options,type=type,regions=regions,district=district,communes=communes,user_id=user_id)
            articles.save()
            lastId = Article.objects.latest('id').id
            return render(request, 'insertion_du_produit.html',{'form':form ,"id":lastId})
        else:
            for field in form.errors:
               form[field].field.widget.attrs['class'] += " is-invalid "
            return render(request, 'insertion_du_produit.html',{'form':form})
    else:
        return render(request, 'insertion_du_produit.html', {'form':form})
    

        # 'id': id_article
    #if request.method=="POST":
     #   form = ArticleForm(request.POST)
        #if form.is_valid():
            #titre = request.POST['titre']
            #race = request.POST['race']
           
                       
            
        #else:
         #   return render(request, 'insertion_du_produit.html', {'form':form})
    
def ArticlePhotoP(request, lastId):
    if request.method=='POST':
        form = ArticlePhotoForm(request.POST, request.FILES)
        if form.is_valid():
            image1 = request.FILES['image1']
            image2 = request.FILES['image2']
            image3 = request.FILES['image3']
            image4 = request.FILES['image4']
            lastId = request.POST['lastId']
            photo = ArticlePhoto(image1=image1,image2=image2,image3=image3,image4=image4,article_id=lastId)
            photo.save()
            #img_obj = ArticlePhoto.instance
            return redirect("myAdmin")
    else:
        form = ArticlePhotoForm()
    return render(request, 'ArticlePhoto.html', {'form':form, 'lastId':lastId})
        

def listeAdmin(request):
    User = get_user_model()
    myAdminListe = User.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(myAdminListe, 10)
    try:
        myAdminListe = paginator.page(page)
    except PageNotAnInteger:
        myAdminListe = Paginator.page(1)
    except EmptyPage:
        myAdminListe = paginator.page(paginator.num_pages)
    #print(myAdminListe)
    
    return render(request, 'listeAdmin.html',{'myAdminListe':myAdminListe})


def OffreTandegna(request):
    OffreTandegna = Article.objects.filter(options='Offre')
    image = ArticlePhoto.objects.all()
    return render(request, 'OffreTandegna.html',{'OffreTandegna':OffreTandegna,"image":image})

def DemandeTandegna(request):
    DemandeTandegna = Article.objects.filter(options='Demande')
    image = ArticlePhoto.objects.all()
    return render(request, 'DemandeTandegna.html',{'DemandeTandegna':DemandeTandegna,"image":image})


def details_tandegna(request, id):
    details_tandegna = Article.objects.get(id=id)
    # details_tandegna = details_tandegna.GET.get('details_articles',1)

    image = ArticlePhoto.objects.all()

    return render(request, 'details_tandegna.html', {'details_tandegna':details_tandegna, 'image':image})

def mode_Tandegna(request):
    return render(request, "mode_Tandegna.html")


def detailsAdmin(request):
    return render(request,'detailsAdmin.html')

#def ArticlePhoto(request, id_article):
# 

def stockArticle(request):
    formStockArticle = StockForm()
    

    if request.method == "POST":
        formStockArticle = StockForm(request.POST)
        nombre = request.POST['nombre']
        id_article = request.POST['id_article']
        if formStockArticle.is_valid():
            stockArticle = Stock(nombre=nombre,article_id=id_article)
            stockArticle.save()
            messages.error(request, "Enregistrement effectué...!")
            return redirect('insertion_du_produit')            
        else:
            formStockArticle = StockForm()
    return render(request, 'insertion_du_produit.html',{'formStockArticle':formStockArticle})

