from django.urls import path
import views


urlpatterns = [
    path('ajouter_hotel/',views.views.ajouter_hotel, name='ajouter_hotel'),
    path('modifier_hotel/<str:pk>/',views.modifier_hotel,name='modifier_hotel'),
    path('supprimer_hotel/<str:pk>/',views.supprimer_hotel, name='supprimer_hotel'),
    path('all_hotels/',views.lire_hotels, name='all_hotels'),
]
