from django.urls import path
from .views import *


urlpatterns = [
    path('signup/',signup_page, name='signup_page'),
    path('login/',login_page, name='login_page'),
    path('logout/',logout_page, name='logout_page'),
    path('home/',home_account, name='home_account'),
]
