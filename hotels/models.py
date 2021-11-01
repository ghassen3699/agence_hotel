from django.db import models
from django.contrib.auth.models import User


class Hotel(models.Model) :


    # les donnees de l'hotel
    compte = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    nom = models.CharField(max_length=30,null=True)
    adresse = models.CharField(max_length=100,null=True)
    image = models.ImageField(blank=True,null=True)
    email = models.EmailField(unique=True,null=True)
    numero_telephone = models.CharField(max_length=8,null=True)
    
    # les catacteristiques de l'hotel
    nombre_des_chambres = models.IntegerField(null=True)
    nombre_des_etoiles = models.IntegerField(null=True)
    


    def __str__(self) :
        return self.nom

