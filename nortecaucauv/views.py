# nortecaucauv/views.py

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'almuerzos_uv/index.html')


def index(request):
    return render(request, 'almuerzos_uv/index.html')