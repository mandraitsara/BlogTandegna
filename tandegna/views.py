import time
from django.http import Http404
from django.views.generic.edit import UpdateView, CreateView,DeleteView
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
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings



#def handler500(request, exception):
#    return render(request, '500.html', status=500)


def home(request):
    usersPresta = User.objects.all()
    liste_articles = Article.objects.all()   
    form = LoginForm()
    page = request.GET.get('page',1)
    paginator = Paginator(liste_articles, 12)
    #options = Article.objects.get(options='demande')
    image = ArticlePhoto.objects.all()
    stock = Stock.objects.all() 

    

    
    try:
        article = paginator.page(page)
    except PageNotAnInteger:
        article = Paginator.page(1)
    except EmptyPage:
        article = paginator.page(paginator.num_pages)
    context = {
        'liste_articles':article,
        'form':form,
        'image':image,
        'stockArticle':stock,
        'users':usersPresta,
    }

    return render(request, 'index.html', context )
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
    
def montuple(request):
    choices = ('Landrace','Large White','Middle White','Omby Manga','Omby Mena')
    x = 1
    liste = Article.objects.all()
    fruits = ("apple",'orange',"banana")
    y = ("1","2","4","5","6")
    for i in range(3):
        print(fruits[i])
        for n in y:
            if i == n:
                print(n)
                print(i)
                print("ok")
                print(fruits.__getitem__(i))
            else:
                print("ko")
                
                             

        
        
       

    

             
       
 #   for tulpes in choices:
 #       if tulpes.__getitem__(int(p)):
 #           affiche = tulpes.__getitem__(int(p))
 #           print(affiche) 

    template = "montuple.html"
    context = {
        #"affiche" :affiche,
        "liste":liste,
    }
    return render(request, template, context)


def mailTandegna(request):
    if request.method == 'POST':
        recipient = "pmandraitsara@gmail.com"
        subject = request.POST['subject']
        message = request.POST['message']
                # send the email to the recipent
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL,[recipient])                
        messages.success(request,'email bien envoyé...')
        return redirect("home")
    else:
        return redirect("home")


def inscription_tandegna(request):
    form =  InscriptionForm()
    if request.method=="POST":
        form = InscriptionForm(request.POST)
        telephone = request.POST['telephone']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password=  request.POST['password']
        typeCompte = request.POST['typeCompte']
        email= request.POST['email']
        passwordC=  request.POST['passwordC']

        
        if len(first_name)<=3:
            messages.error(request, 'Le nom est vraiment court')
            return render(request, 'inscription_tandegna.html',{'form':form})
        
        if len(last_name)<=3:
            messages.error(request, 'Le prenom est vraiment court')
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
            user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,email=email,telephone=telephone,typeCompte=typeCompte)         

            if user is not None:
                return redirect('login_tandegna')
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
            categories = request.POST['categories']
            regions = request.POST['regions']
            district = request.POST['district']
            communes = request.POST['communes']
            prix = request.POST['prix']
            adresseComplet = request.POST['adresseComplet']
            telephone = request.POST['telephone']
            telephoneB = request.POST['telephoneB']
            user_id = request.POST['user_id']

            
            #images = request.POST['images']
            articles = Article(titre=titre,race=race,ages=ages,description=description,poids=poids,options=options,categories=categories,regions=regions,district=district,communes=communes,adresseComplet=adresseComplet, telephone=telephone, telephoneB=telephoneB,prix=prix, user_id=user_id)
            articles.save()
            lastId = Article.objects.latest('id').id
            messages.success(request, "insertion effectuée....")
            return render(request, 'insertion_du_produit.html',{'form':form ,"lastId":lastId})
        else:
            for field in form.errors:
               form[field].field.widget.attrs['class'] += " is-invalid "
            messages.error(request, "insertion échouée....")
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

def mon_compte(request, slug, id):
    id_user = User.objects.get(slug=slug, id=id)
    
    context = {
        "id_user":id_user
    }
    

    return render(request, "mon_compte.html",context)

def ArticlePhotoView(request,lastId):
    lastId = Article.objects.get(id=lastId)
    formPhoto = ArticlePhotoForm(request.FILES, request.POST)
    # form = ArticleForm() 
    if request.method =="POST":
                formPhoto = ArticlePhotoForm(request.FILES, request.POST)
                image1 = request.FILES["image1"]
                image2 = request.FILES["image2"]
                image3 = request.FILES["image3"]
                image4 = request.FILES["image4"]
                lastId = request.POST["lastId"]
                photo = ArticlePhoto(image1=image1,image2=image2,image3=image3,image4=image4,article_id=lastId)
                photo.save()
                myLast = ArticlePhoto.objects.latest('id').id
                messages.error(request, "enregistrement effectué")
                context = {
                    'fomrPhoto':formPhoto,
                    'id':lastId,
                    'myLast':myLast
                }
                return render(request, 'ArticlePhoto.html',context)
    else:
        return render(request, 'ArticlePhoto.html', {'formPhoto':formPhoto,'id':lastId})


def ArticlePhotoViewEdit(request, id):
    form = ArticlePhotoForm(request.POST, request.FILES)
    myEdit = ArticlePhoto.objects.get(id=id)
    context = {
        'form':form,
        'myEdit':myEdit       
        }
    
    if request.method == "POST":
        if form.is_valid():
            image1 = request.FILES['image1']
            image2 = request.FILES['image2']
            image3 = request.FILES['image3']
            image4 = request.FILES['image4']
            myEdit.image1 = image1
            myEdit.image2 = image2
            myEdit.image3 = image3
            myEdit.image4 = image4   
            myEdit.save()
            messages.success(request, "La valeur est bien modifié")
            return render(request, 'ArticlePhoto_Edit.html', context)
        else:
            messages.error(request, ": impossible de faire la modification")
            return render(request, 'ArticlePhoto_Edit.html', context)        
    else:
        return render(request, 'ArticlePhoto_Edit.html',context)

  
    

  
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
    page = request.GET.get('page', 1)
    paginator = Paginator(OffreTandegna, 9)
    #options = Article.objects.get(options='demande')
    image = ArticlePhoto.objects.all()

    try:
        OffreTandegna = paginator.page(page)
    except PageNotAnInteger:
        OffreTandegna = Paginator.page(1)
    except EmptyPage:
        OffreTandegna = paginator.page(paginator.num_pages)

    
    image = ArticlePhoto.objects.all()

    return render(request, 'OffreTandegna.html',{'OffreTandegna':OffreTandegna,"image":image})

def DemandeTandegna(request):
    DemandeTandegna = Article.objects.filter(options='Demande')
    image = ArticlePhoto.objects.all()
    return render(request, 'DemandeTandegna.html',{'DemandeTandegna':DemandeTandegna,"image":image})


def details_tandegna(request, slug, id):
    details_tandegna = Article.objects.get(slug=slug, id=id)
    image = ArticlePhoto.objects.all()

    context = {
        'details_tandegna':details_tandegna,
        'image':image
    }

    return render(request, 'details_tandegna.html', context)

def mode_Tandegna(request):
    return render(request, "mode_Tandegna.html")


def detailsAdmin(request):
    return render(request,'detailsAdmin.html')

#def ArticlePhoto(request, id_article):


# 

def filtreTandegna(request):
    template = "filtreTandegna.html"
    stock = Stock.objects.all()
    image = ArticlePhoto.objects.all()
    usersPresta = User.objects.all()
    

    if request.method == "POST":
        options = request.POST["options"]
        categories = request.POST["categories"]        
        race = request.POST["race"]

        article_filtres = Article.objects.filter(categories__contains=categories, options__contains=options, race__contains=race)
        #option = Article.objects.filter(options__contains=options)
        #racy = Article.objects.filter(race__contains=race)

        
        context = {
        "options":options,
        "categories":categories,        
        "race":race,
        "image":image,
        "stockArticle":stock,
        "users":usersPresta,
       "article":article_filtres,
        }
        
        return render(request, template,context)
    else:
        return render(request, template)





def rechercheTandegna(request):
#    GET={"article":"cafe"}
       
       
    stock = Stock.objects.all()

    image = ArticlePhoto.objects.all()
    usersPresta = User.objects.all()
    
    query = request.GET['RechercheArticleTandegna']
    
    #tous = request.GET['tous']
    #filter = request.GET['page']
    if query == '':
        return redirect('home')
    
    liste_article = Article.objects.filter(titre__contains=query)  or Article.objects.filter(prix__contains=query) or Article.objects.filter(options__contains=query) or Article.objects.filter(devise__contains=query)
    context = {
        "liste_article":liste_article,
        "image":image,
        "stockArticle":stock,
        "users":usersPresta,
        "query":query,
    }
    
    return render(request, 'rechercheTandegna.html',context)




def stockArticle(request, lastId):
    formStockArticle = StockForm()
    article = Article.objects.get(id=lastId)    
    if request.method == "POST":
        formStockArticle = StockForm(request.POST)
        nombre = request.POST['nombre']
        unites = request.POST['unites']
        id_article = request.POST['id_article']
        if id_article=="":
            messages.error(request, "impossible d\'effectuer l\'enregistrement")
            return render(request, 'ArticleStock.html',{'formStockArticle':formStockArticle,'id_article':article})
        if formStockArticle.is_valid():
            stockArticle = Stock(nombre=nombre,unites=unites,article_id=str(id_article))
            stockArticle.save()
            messages.error(request, "Enregistrement effectué...!")
            return render(request, 'ArticleStock.html',{'formStockArticle':formStockArticle,'id_article':article})            
        else:
            formStockArticle = StockForm()
    return render(request, 'ArticleStock.html',{'formStockArticle':formStockArticle,'id_article':article})



    

def handler404(request, exception):
    return render(request, '404.html', status=404)