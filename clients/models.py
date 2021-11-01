from django.db import models
from django.contrib.auth.models import User



class Client(models.Model) :

    compte = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    email = models.EmailField(unique=True,null=True)
    nom = models.CharField(max_length=30,null=True)
    prenom = models.CharField(max_length=30,null=True)
    age = models.IntegerField(null=True)
    GENRE = [
        ('HOMME','Homme'),
        ('FEMME','Femme'),
    ]
    genre = models.CharField(choices=GENRE,max_length=10,null=True)
    numero_telephone = models.CharField(max_length=8,null=True)

    def __str__(self) :
        return '{} {}'.format(self.nom, self.prenom)