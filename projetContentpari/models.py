from django.db import models

# Create your models here.



# User table.
# class User(models.Model):
#     name = models.CharField(max_length=120)
#     username = models.CharField(max_length=42)
#     numero = models.CharField(max_length=42)
#     email = models.EmailField(max_length=75)
#     nbr_joueur = models.EmailField(max_length=100)
#     password = models.EmailField(max_length=200, null=False, blank=False)
    




class userPari(models.Model):
    idPari = models.CharField(max_length=200, null=False, blank=False, default="0")
    montantParier = models.CharField(max_length=200, null=False, blank=False , default="0")
    status = models.CharField(max_length=200, null=False, blank=False, default="")
    datePari = models.CharField(max_length=200)
    namePari = models.CharField(max_length=120)
    nameUser = models.CharField(max_length=200, null=False, blank=False, default="XXXX")
    idUser = models.CharField(max_length=200, null=False, blank=False, default="0")
    
    def __str__(self):
        return self.name





class pariListe(models.Model):
    namePari = models.CharField(max_length=120)
    montantMin = models.CharField(max_length=200, null=False, blank=False)
    montantMax = models.CharField(max_length=200, null=False, blank=False)
    pourcentage = models.CharField(max_length=200, null=False, blank=False)
    dateDebut = models.CharField(max_length=200, null=False, blank=False)
    dateFin = models.CharField(max_length=200, null=False, blank=False)
    nbreEquipeMin = models.CharField(max_length=200, null=False, blank=False)
    nbreEquipeMax = models.CharField(max_length=200, null=False, blank=False)

