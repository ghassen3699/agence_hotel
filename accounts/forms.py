from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



# la formulaire de creation compte
class UserFormulaire(UserCreationForm) :
    class Meta :
        model = User
        fields = ('username','password1','password2')