from django.contrib import admin
from django.urls import path, include
from. import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('registrar_edificios/', views.registrar_edificios, name='registrar_edificios'),
    path('registrar_estudiantes/', views.registrar_estudiantes, name='registrar_estudiantes'),
    path('listado_edificios/', views.listado_edificios, name='listado_edificios'),
    path('editar_edificios/<str:numero>/', views.editar_edificios, name='editar_edificios'),
    path('add_persona/', views.add_persona, name='add_persona'),
    path('listado_estudiantes/', views.listado_estudiantes, name='listado_estudiantes'),
    path('editar_estudiantes/<str:id>/', views.editar_estudiantes, name='editar_estudiantes'),
    path('mostrar_estudiantes/<str:id>/', views.mostrar_estudiantes, name='mostrar_estudiantes'),
    path('eliminar_estudiantes/<str:id>/', views.eliminar_estudiantes, name='eliminar_estudiantes'),
    # path('actualizar_Estudiante/<str:solapin>/', views.actualizar_Estudiante, name='Actualizar estudiante'),
]


