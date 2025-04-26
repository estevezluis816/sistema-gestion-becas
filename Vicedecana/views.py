from django.shortcuts import render, redirect, get_object_or_404
from .models import Edificios, Estudiantes
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import EstudianteForm, EdificioForm
from django.db import IntegrityError


def inicio(request):
    return render(request, "index.html")


def registro(request):
    return render(request, "registro.html")


def registrar_edificios(request):
    if request.method == 'POST':
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
    if request.method == 'POST':
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
    edificios = Edificios.objects.all()
    return render(request, "edificios.html", {'edificios': edificios})


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

    ano = request.GET.get('ano', '').strip()
    carrera = request.GET.get('carrera', '').strip()

    if ano:
        estudiantes = estudiantes.filter(grade=ano)
    if carrera:
        estudiantes = estudiantes.filter(carrera__icontains=carrera)

    return render(request, "estudiantes.html", {
        'estudiantes': estudiantes,
        'ano': ano,
        'carrera': carrera
    })


def mostrar_estudiantes(request, id):
    try:
        estudiante = Estudiantes.objects.get(pk=id)
    except Estudiantes.DoesNotExist:
        return render(request, "mostrarEstudiante.html", {'estudiante': None})
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


def buscar(request):
    query = request.GET.get('q', '').strip()
    query_ano = request.GET.get('ano', '').strip()
    query_carrera = request.GET.get('carrera', '').strip()

    estudiantes = Estudiantes.objects.all()
    edificios = Edificios.objects.all()

    if query:
        estudiantes = estudiantes.filter(full_name__icontains=query) | estudiantes.filter(usuario__icontains=query)
        edificios = edificios.filter(numero__icontains=query)

    if query_ano:
        estudiantes = estudiantes.filter(grade__icontains=query_ano)
        edificios = Edificios.objects.filter(ano__icontains=query_ano)

    if query_carrera:
        estudiantes = estudiantes.filter(carrera__icontains=query_carrera)
        edificios = Edificios.objects.filter(carrera__icontains=query_carrera)

    return render(request, "buscar.html", {
        'query': query,
        'query_ano': query_ano,
        'query_carrera': query_carrera,
        'estudiantes': estudiantes.distinct(),
        'edificios': edificios.distinct(),
    })
