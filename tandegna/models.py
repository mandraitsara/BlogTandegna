from django.db import models
#from __future__ import unicode_literals
from django.contrib.auth.models import User

class Category(models.Model):
    titre = models.CharField(null=True, max_length=10)
    name= models.CharField(max_length=120)

# Create your models here.
class Article(models.Model):
    #category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    titre = models.CharField(max_length=30)
    race = models.CharField(max_length=15)
    ages = models.CharField(max_length=20)
    description = models.CharField(max_length=250)
    poids = models.CharField(max_length=10)
    options = models.CharField(max_length=20)
    type = models.CharField(max_length=10)
    regions = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    communes = models.CharField(max_length=30)
    
    created=models.DateTimeField(auto_now_add=True)
    created_by = models.DateTimeField(auto_now=True)

class Members(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    adresse = models.CharField(max_length=20)
    telephone = models.CharField(max_length=10)
    puce = models.CharField(max_length=10)
    
class ArticlePhoto(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
 #   article_id = models.CharField(max_length=150)
    image1 = models.FileField()
    image2 = models.FileField()
    image3 = models.FileField()
    image4 = models.FileField()

class Historique(models.Model):
    titre = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

class Stock(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=100)
    created_by = models.DateTimeField(auto_now_add=True)

