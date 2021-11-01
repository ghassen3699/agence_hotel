from django.db import models
from django.db.models.deletion import SET_NULL
from django.contrib.auth.models import User
from hotels.models import Hotel



class Reservation(models.Model) :
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True)
    nombre_des_jours = models.PositiveIntegerField(null=True)
    date_de_debut = models.DateField()
    date_de_fin = models.DateField()



    def __str__(self) :
        return self.user