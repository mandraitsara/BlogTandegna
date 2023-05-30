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
    slug = models.CharField(default="TandegnaArticle_slugSpecialeVraiment+match=idpv_", max_length=250)
    race = models.CharField(max_length=15)
    ages = models.CharField(max_length=20)
    description = models.CharField(max_length=250)
    poids = models.CharField(max_length=10)
    options = models.CharField(max_length=20)
    categories = models.CharField(max_length=140)
    regions = models.CharField(max_length=250)
    district = models.CharField(max_length=250)
    communes = models.CharField(max_length=250)
    prix = models.CharField(max_length=200)
    telephone = models.CharField(max_length=10)
    telephoneB = models.CharField(max_length=10, null=True)
    adresseComplet = models.CharField(max_length=150)
    created=models.DateTimeField(auto_now_add=True)
    created_by = models.DateTimeField(auto_now=True)
    devise = models.CharField(max_length=20, default="Ar")
    
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
    nombre = models.CharField(max_length=1000)
    unites = models.CharField(max_length=3)
    created_by = models.DateTimeField(auto_now_add=True)

