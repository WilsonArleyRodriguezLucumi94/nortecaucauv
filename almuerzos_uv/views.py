from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import AlmuerzoForm
from .models import Estudiante
# Create your views here.

def registrar_almuerzo(request):
    if request.method == 'POST':
        form = AlmuerzoForm(request.POST)
        if form.is_valid():
            almuerzo = form.save(commit=False)
            almuerzo.fecha = timezone.now().date()  # Asigna la fecha actual automáticamente
            almuerzo.save()
            return redirect('almuerzos_uv:registrar_almuerzo')  # Redirige a la misma página después de guardar
    else:
        form = AlmuerzoForm()
    return render(request, 'almuerzos_uv/registrar_almuerzo.html', {'form': form})


# almuerzos_uv/views.py

from django.shortcuts import render, redirect
from .forms import EstudianteForm

def registrar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('almuerzos_uv:registrar_estudiante')
    else:
        form = EstudianteForm()
    return render(request, 'almuerzos_uv/registrar_estudiante.html', {'form': form})


def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'almuerzos_uv/lista_estudiantes.html', {'estudiantes': estudiantes})

def index_almuerzos(request):
    return render(request, 'almuerzos_uv/index.html')