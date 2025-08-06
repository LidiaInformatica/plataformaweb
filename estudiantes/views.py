from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenida a la app Estudiantes")

def lista_estudiantes(request):
    return HttpResponse("Listado de estudiantes")

def detalle_estudiante(request, id):
    return HttpResponse(f"Detalle del estudiante con ID {id}")
