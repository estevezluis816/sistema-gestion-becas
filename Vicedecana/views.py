from django.shortcuts import render, redirect, get_object_or_404
from .models import Edificios, Estudiantes, Apartamento
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
            edificio = form.save()
            cantidad_apartamentos = form.cleaned_data['cantidad_apartamentos']

            # Crear apartamentos automáticamente
            for i in range(1, cantidad_apartamentos + 1):
                if i <= 8:
                    numero_apto = f"10{i}"
                elif 9 <= i <= 16:
                    numero_apto = f"20{i-8}"
                elif 17 <= i <= 24:
                    numero_apto = f"30{i-16}"
                else:
                    numero_apto = f"{i:03d}"

                Apartamento.objects.create(
                    numero=numero_apto,
                    edificio=edificio,
                    disponibilidad=True
                )
            return redirect('listado_edificios')
        else:
            return render(request, "registroEdificios.html", {'form': form})
    else:
        form = EdificioForm()
        return render(request, "registroEdificios.html", {'form': form})

def registrar_estudiantes(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado_estudiantes')
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
            edificio = form.save()
            cantidad_apartamentos = form.cleaned_data['cantidad_apartamentos']

            # Eliminar apartamentos anteriores
            Apartamento.objects.filter(edificio=edificio).delete()

            # Crear apartamentos nuevos
            for i in range(1, cantidad_apartamentos + 1):
                if i <= 8:
                    numero_apto = f"10{i}"
                elif 9 <= i <= 16:
                    numero_apto = f"20{i-8}"
                elif 17 <= i <= 24:
                    numero_apto = f"30{i-16}"
                else:
                    numero_apto = f"{i:03d}"

                Apartamento.objects.create(
                    numero=numero_apto,
                    edificio=edificio,
                    disponibilidad=True
                )

            return redirect('listado_edificios')
        else:
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
    estudiante = get_object_or_404(Estudiantes, pk=id)
    return render(request, "mostrarEstudiante.html", {'estudiante': estudiante})

def editar_estudiantes(request, id):
    estudiante = get_object_or_404(Estudiantes, pk=id)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('mostrar_estudiantes', id)
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
        edificios = edificios.filter(ano__icontains=query_ano)

    if query_carrera:
        estudiantes = estudiantes.filter(carrera__icontains=query_carrera)
        edificios = edificios.filter(carrera__icontains=query_carrera)

    return render(request, "buscar.html", {
        'query': query,
        'query_ano': query_ano,
        'query_carrera': query_carrera,
        'estudiantes': estudiantes.distinct(),
        'edificios': edificios.distinct(),
    })
