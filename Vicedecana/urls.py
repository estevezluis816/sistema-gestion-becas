from django.contrib import admin
from django.urls import path, include
from . import views  # Asegúrate de que la importación esté correcta

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('registrar_edificios/', views.registrar_edificios, name='registrar_edificios'),
    path('registrar_estudiantes/', views.registrar_estudiantes, name='registrar_estudiantes'),
    path('listado_edificios/', views.listado_edificios, name='listado_edificios'),
    path('listado_estudiantes/', views.listado_estudiantes, name='listado_estudiantes'),
    path('editar_edificios/<int:numero>/', views.editar_edificios, name='editar_edificios'),  # ID del edificio como entero
    path('editar_estudiantes/<str:id>/', views.editar_estudiantes, name='editar_estudiantes'),  # ID del estudiante como cadena
    path('mostrar_estudiantes/<str:id>/', views.mostrar_estudiantes, name='mostrar_estudiantes'),  # ID del estudiante como cadena
    path('eliminar_estudiantes/<str:id>/', views.eliminar_estudiantes, name='eliminar_estudiantes'),  # ID del estudiante como cadena
    path('obtener_apartamentos/<int:edificio_id>/', views.obtener_apartamentos, name='obtener_apartamentos'), # ID del edificio como entero
    path('buscar/', views.buscar, name='buscar'),
]
