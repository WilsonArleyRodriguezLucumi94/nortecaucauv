# almuerzos_uv/urls.py


from django.urls import path
from . import views

app_name = 'almuerzos_uv'

urlpatterns = [
    path('registrar/', views.registrar_almuerzo, name='registrar_almuerzo'),
    path('registrar_estudiante/', views.registrar_estudiante, name='registrar_estudiante'),
    path('lista_estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),
    path('index_almuerzos/', views.index_almuerzos, name='index_almuerzos'),
]
