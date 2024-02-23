from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Création de modèle pour le infoBoutique

class infoBoutique(models.Model):
    adresse = models.CharField(max_length=150)
    lot = models.CharField(max_length=150)
    mail = models.CharField(max_length=150)
    telephone = models.CharField(max_length=150)
    codepostal = models.CharField(max_length=150)
    fax = models.CharField(max_length=150)
    
class workflow(models.Model):
    titre = models.CharField(max_length=200)
    iso = models.CharField(max_length=150)
    liens = models.CharField(max_length=200)

class subscribModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=200,)
    pack = models.CharField(max_length=200,null=True,default='null')
    phone = models.CharField(max_length=200 ,null=True)
    commentaire = models.CharField(max_length=200,null=True)

class produitCategory(models.Model):
    titre = models.CharField(max_length=150, null=True)

class produitRace(models.Model):
    produitcategory = models.ForeignKey(produitCategory, on_delete=models.CASCADE, null=True)
    titre = models.CharField(max_length=150, null=True)

class produits(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    produit_category = models.ForeignKey(produitCategory,on_delete=models.CASCADE, null=True)
    produit_race = models.ForeignKey(produitRace,on_delete=models.CASCADE, null=True)
    titre = models.CharField(max_length=150, null=True)
    description = models.CharField(max_length=150, null=True)
    prix = models.CharField(max_length=150, null=True)
    devise = models.CharField(max_length=150, null=True)
    photo_p = models.FileField(max_length=200)
    photo_s = models.FileField(max_length=200)
    photo_tr = models.FileField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.DateTimeField(auto_now=True)

# class produitPhoto(models.Model):
#     produit = models.ForeignKey(produits,on_delete=models.CASCADE, null=True)
#     photos1 = models.CharField(max_length=150, null=True)
#     photos2 = models.CharField(max_length=150, null=True)
#     photos3 = models.CharField(max_length=150, null=True)

class produitStock(models.Model):
    produit = models.ForeignKey(produits,on_delete=models.CASCADE, null=True)
    nbr_debut = models.CharField(max_length=150, null=True)
    nbr_consomme = models.CharField(max_length=150, null=True)
    nbr_reste = models.CharField(max_length=150, null=True)



