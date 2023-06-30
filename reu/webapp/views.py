from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from estudiantes.models import Estudiante
# Create your views here.

def mostrar_estudiantes(request):
    cantidad_estudiantes = Estudiante.objects.count()
    pagina = loader.get_template('estudiantes.html')
    nombres_estudiantes = Estudiante.objects.all()
    nombres_estudiantes = Estudiante.objects.order_by('apellido', 'nombre')
    datos = {'cantidad': cantidad_estudiantes, 'estudiantes': nombres_estudiantes}

    return HttpResponse(pagina.render(datos, request))