# almuerzos_uv/forms.py

from django import forms
from .models import Almuerzo

class AlmuerzoForm(forms.ModelForm):
    class Meta:
        model = Almuerzo
        fields = ['cantidad']


# almuerzos_uv/forms.py

from django import forms
from .models import Estudiante

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['codigo_estudiante', 'nombre_estudiante', 'apellido_estudiante', 'plan_estudiante', 'correo_estudiante']
