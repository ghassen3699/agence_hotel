from django.forms import ModelForm
from .models import Client



class ClientFormulaire(ModelForm) :
    class Meta :
        model = Client
        fields = ('nom','prenom','email','age','genre','numero_teliphone')