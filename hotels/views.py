from django.db import models
from django.shortcuts import redirect, render, get_object_or_404
from .forms import HotelFormulaire
from .models import Hotel
from django.contrib import messages




# ajouter un hotel a la base de donnees 
def ajouter_hotel(request) :
    formulaire_hotel = HotelFormulaire()

    if request.method == "POST" :
        formulaire_hotel = HotelFormulaire(request.POST)
        if formulaire_hotel.is_valid() :
            formulaire_hotel.save()
            return redirect('login_page')
    
    return render(request,'hotels/ajouter_hotel.html',{'formulaire_hotel':formulaire_hotel})


# modifier les donnees de l'hotel
def modifier_hotel(request, pk) :

    try :
        hotel = Hotel.objects.get(id= pk)
    except Hotel.DoesNotExist :
        return render(request,'hotels/404_erreur.html')
    
    formulaire_hotel = HotelFormulaire(instance=hotel)

    if request.method == "POST" :
        formulaire_hotel = HotelFormulaire(request.POST,instance=hotel)
        if formulaire_hotel.is_valid() :
            formulaire_hotel.save()
            messages.success(request,"La Modification L'hotel Est Enregistrer Avec Success")
        else :
            messages.info(request,'Entrer Correctement Vos Donnees')
    
    return render(request,'hotels/modifier_hotel.html',{'formulaire_hotel':formulaire_hotel})


# lire tout les hotels
def lire_hotels(request) :

    try :
        hotels = Hotel.objects.all()
    except Hotel.DoesNotExist :
        return render(request,'all_hotels.html',{'message':'Désole On a Aucun Hotel Disponible :\ '})

    return render(request,'hotels/all_hotel.html',{'hotels':hotels})


# supprimer un hotel
def supprimer_hotel(request, pk) :

    try :
        hotel = Hotel.objects.get(id= pk)
    except Hotel.DoesNotExist :
        return render(request,'hotels/404_erreur.html')
    
    if request.method == "POST" :
        hotel.delete()
    
    return redirect('home_account')