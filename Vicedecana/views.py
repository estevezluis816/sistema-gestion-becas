from django.shortcuts import render, redirect, get_object_or_404
from .models import Edificios, Estudiantes
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import EstudianteForm, EdificioForm
from django.db import IntegrityError


# Create your views here.

def inicio(request):
    return render(request, "index.html")


def registro(request):
    return render(request, "registro.html")


def registrar_edificios(request):
    if request.method =='POST':
        form = EdificioForm(request.POST)
        if form.is_valid():
            form.save()
            form = EdificioForm()
            return redirect("registrar_edificios")
        else:
            return render(request, "registroEdificios.html", {'form': form})
    else:
        form = EdificioForm()
        return render(request, "registroEdificios.html", {'form': form})
    
def add_persona(request):

    return render(request, "anadirPersona.html")


def registrar_estudiantes(request):
    if request.method =='POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            form = EstudianteForm()
            return redirect("registrar_estudiantes")
        else:
            return render(request, "registroEstudiantes.html", {'form': form})
    else:
        form = EstudianteForm()
        return render(request, "registroEstudiantes.html", {'form': form})


def listado_edificios(request):
    edificios= Edificios.objects.all()
    return render(request, "edificios.html", {'edificios':edificios})


# views.py
def editar_edificios(request, numero):
    edificio = get_object_or_404(Edificios, pk=numero)
    if request.method == 'POST':
        form = EdificioForm(request.POST, instance=edificio)
        if form.is_valid():
            form.save()
            return redirect('listado_edificios')
        else:
            try:
                form.save(commit=False)
                form.save_m2m()
            except IntegrityError:
                pass
            return render(request, "editarEdificio.html", {'form': form})
    else:
        form = EdificioForm(instance=edificio)
    return render(request, "editarEdificio.html", {'form': form})


def listado_estudiantes(request):
    estudiantes = Estudiantes.objects.all()
    return render(request, "estudiantes.html", {'estudiantes':estudiantes})


def mostrar_estudiantes(request, id):
    try:
        estudiante = Estudiantes.objects.get(pk=id)
    except Estudiantes.DoesNotExist:
        return render(request, "mostrarEstudiante.html", {'estudiante': estudiante})
    else:
        return render(request, "mostrarEstudiante.html", {'estudiante': estudiante})


def editar_estudiantes(request, id):
    estudiante = get_object_or_404(Estudiantes, pk=id)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('mostrar_estudiantes', id)
        else:
            try:
                form.save(commit=False)
                form.save_m2m()
            except IntegrityError:
                pass
            return render(request, "editarEstudiante.html", {'form': form})
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, "editarEstudiante.html", {'form': form})


def eliminar_estudiantes(request, id):
    estudiante = get_object_or_404(Estudiantes, pk=id)
    estudiante.delete()
    return redirect('listado_estudiantes')