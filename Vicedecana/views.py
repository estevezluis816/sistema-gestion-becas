from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudiantes, Apartamento, Edificios
from .forms import EstudianteForm, EdificioForm
from django.contrib import messages
from django.http import JsonResponse


# Página principal
def inicio(request):
    return render(request, "index.html")

# Vista para el registro de un nuevo edificio
def registro(request):
    return render(request, "registro.html")

# Registrar un nuevo edificio con la creación de apartamentos
def registrar_edificios(request):
    if request.method == 'POST':
        form = EdificioForm(request.POST)
        if form.is_valid():
            edificio = form.save()
            cantidad_apartamentos = form.cleaned_data['cantidad_apartamentos']

            # Crear apartamentos automáticamente
            for i in range(1, cantidad_apartamentos + 1):
                numero_apto = generar_numero_apartamento(i)
                Apartamento.objects.create(
                    numero=numero_apto,
                    edificio=edificio,
                    disponibilidad=True
                )
            messages.success(request, f"Edificio {edificio.numero} registrado con éxito.")
            return redirect('listado_edificios')
        else:
            messages.error(request, "Error al registrar el edificio.")
            return render(request, "registroEdificios.html", {'form': form})
    else:
        form = EdificioForm()
        return render(request, "registroEdificios.html", {'form': form})

# Función para generar el número de apartamento
def generar_numero_apartamento(i):
    if i <= 8:
        return f"10{i}"
    elif 9 <= i <= 16:
        return f"20{i-8}"
    elif 17 <= i <= 24:
        return f"30{i-16}"
    else:
        return f"{i:03d}"

# Listar todos los edificios
def listado_edificios(request):
    edificios = Edificios.objects.all()
    return render(request, "edificios.html", {'edificios': edificios})

# Editar un edificio y actualizar apartamentos
def editar_edificios(request, numero):
    edificio = get_object_or_404(Edificios, pk=numero)
    if request.method == 'POST':
        form = EdificioForm(request.POST, instance=edificio)
        if form.is_valid():
            edificio = form.save()
            cantidad_apartamentos = form.cleaned_data['cantidad_apartamentos']

            # Eliminar apartamentos anteriores y crear nuevos
            Apartamento.objects.filter(edificio=edificio).delete()
            for i in range(1, cantidad_apartamentos + 1):
                numero_apto = generar_numero_apartamento(i)
                Apartamento.objects.create(
                    numero=numero_apto,
                    edificio=edificio,
                    disponibilidad=True
                )
            messages.success(request, f"Edificio {edificio.numero} actualizado con éxito.")
            return redirect('listado_edificios')
        else:
            messages.error(request, "Error al actualizar el edificio.")
            return render(request, "editarEdificio.html", {'form': form})
    else:
        form = EdificioForm(instance=edificio)
        return render(request, "editarEdificio.html", {'form': form})

# Registrar un nuevo estudiante
def registrar_estudiantes(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            estudiante = form.save()

            # Obtenemos el apartamento seleccionado
            apartamento = Apartamento.objects.get(id=request.POST['apartamento'])

            try:
                estudiante.asignar_apartamento(apartamento)  # Usamos el método del modelo Estudiantes para asignar
                messages.success(request, f"Estudiante {estudiante.full_name} registrado con éxito.")
                return redirect('listado_estudiantes')
            except ValueError as e:
                messages.error(request, str(e))  # Si el apartamento no está disponible, mostramos un mensaje de error
                return redirect('registrar_estudiantes')
        else:
            messages.error(request, "Error al registrar el estudiante. Por favor revisa los campos.")
            return render(request, "registroEstudiantes.html", {'form': form})
    else:
        form = EstudianteForm()

        # Si hay un edificio seleccionado, actualizamos los apartamentos
        if 'edificio' in request.GET:
            edificio_id = request.GET.get('edificio')
            form.set_apartamentos(edificio_id)  # Llamamos a la función que actualizará los apartamentos

        return render(request, "registroEstudiantes.html", {'form': form})

# Listar todos los estudiantes con filtros
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

# Obtener los apartamentos disponibles para un edificio
def obtener_apartamentos(request, edificio_id):
    # Filtra los apartamentos del edificio seleccionado que estén disponibles
    apartamentos = Apartamento.objects.filter(edificio_id=edificio_id, disponibilidad=True)
    apartamentos_data = [{"id": apto.id, "numero": apto.numero} for apto in apartamentos]
    return JsonResponse(apartamentos_data, safe=False)

# Buscar estudiantes y edificios por parámetros
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

# Mostrar detalles de un estudiante
def mostrar_estudiantes(request, id):
    estudiante = get_object_or_404(Estudiantes, pk=id)
    return render(request, "mostrarEstudiante.html", {'estudiante': estudiante})

# Editar un estudiante
def editar_estudiantes(request, id):
    estudiante = get_object_or_404(Estudiantes, pk=id)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            messages.success(request, "Estudiante actualizado correctamente.")
            return redirect('mostrar_estudiantes', id=estudiante.id)  # El id debe ser una cadena
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, "editarEstudiante.html", {'form': form})

# Eliminar un estudiante
def eliminar_estudiantes(request, id):
    estudiante = get_object_or_404(Estudiantes, pk=id)
    estudiante.delete()
    messages.success(request, "Estudiante eliminado correctamente.")
    return redirect('listado_estudiantes')
