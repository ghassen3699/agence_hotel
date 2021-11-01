from django import forms
from .models import Hotel


class HotelFormulaire(forms.ModelForm) :
    class Meta :
        model = Hotel
        fields = ('nom','adresse','image','email','numero_teliphone','nombres_des_chambres','nombre_des_etoiles')



