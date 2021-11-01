from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .forms import UserFormulaire
from django.contrib import messages




# fonction de creation du compte
def signup_page(request) :
    formulaire = UserFormulaire()
    if request.method == "POST" :
        formulaire = UserFormulaire(request.POST) 
        if formulaire.is_valid() :
            formulaire.save()
            messages.success(request,'Compte Creer Avec Success')
            return redirect('login_page')
        messages.error(request,'Entrer Correctement Vous Donnees')
    return render(request,'accounts/signup_page.html',{'formulaire':formulaire})





# la fonction de login 
def login_page(request) :
    if request.method == "POST" :
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None :
            login(request, user)
            return redirect('home_account')
        else :
            messages.error(request,'Erreur Username Ou Mot De Passe Incorrecte')
    return render(request,'accounts/login_page.html')




# fonction de logout 
def logout_page(request) :
    logout(request)
    return redirect('login_page')




def home_account(request) :
    return render(request,'accounts/home_account.html')


