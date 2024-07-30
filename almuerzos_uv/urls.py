# almuerzos_uv/urls.py

from django.urls import path
from . import views

app_name = 'almuerzos_uv'

urlpatterns = [
    path('registrar/', views.registrar_almuerzo, name='registrar_almuerzo'),
    path('registrar_estudiante/', views.registrar_estudiante, name='registrar_estudiante'),

]
