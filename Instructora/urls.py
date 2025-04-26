from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.inicio, name="Inicio I"),
    path('edificios/',views.edificios, name='Edificios'),
    path('apartamentos/',views.apartamentos, name='Apartamentos I'),
    path('personas_Apto/',views.personas_Apto, name='Listado de Personas I'),
]