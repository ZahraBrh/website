from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.

class Auteur(models.Model):
    
     id_Chercheur = models.AutoField(primary_key=True) 
     nom=models.CharField(max_length=100)
     prenom= models.CharField(max_length=100)
     dateNais=models.DateField()
     grade=models.CharField(max_length=100)
     labo_affiliation=models.CharField(max_length=100)
     domaine=models.CharField(max_length=100)
     numTel=models.IntegerField(null=True)
     adresse=models.CharField(max_length=100,null=True)
     email=models.EmailField(null=True)
     articls=models.ManyToManyField('Articl',through='Ecrit')

class Articl(models.Model):
    
    idArt=models.AutoField(primary_key=True)
    titre=models.CharField(max_length=250)
    resumé=models.CharField(max_length=500)
    dateEdition=models.DateField()
    maison_ed=models.CharField(max_length=500)
    nbd_cit=models.IntegerField(null=True)
    keywords=models.CharField(max_length=500)
    typeArticl=models.CharField(max_length=100)
    path=models.FilePathField()
    auteurs=models.ManyToManyField('Auteur',through='Ecrit')
    #published_date = models.DateTimeField(blank=True, null=True)

     #def publish(self):
      #  self.published_date = timezone.now()
       # self.save()


class Ecrit(models.Model):
    auteurEcrit = models.ForeignKey(Auteur,on_delete=models.CASCADE)
    articlEcrit = models.ForeignKey(Articl,on_delete=models.CASCADE)
    ordreAuteur =models.IntegerField()
    
  #after any changes: python manage.py makemigrations //// python manage.py migrate  

