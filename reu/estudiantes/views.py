from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from django.forms import modelform_factory
from estudiantes.models import Estudiante
from estudiantes.forms import EstudianteFormulario

# Create your views here.
def agregar_estudiante(request):
    pagina = loader.get_template('agregar_estudiantes.html')
    if request.method == 'GET':
        formulario = EstudianteFormulario
    elif request.method == 'POST':
        formulario = EstudianteFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')

    datos = {'formulario': formulario}
    return HttpResponse(pagina.render(datos, request))

def ver_estudiante(request, idEstudiante):
    pagina = loader.get_template('ver_estudiante.html')
    #estudiante = Estudiante.objects.get(pk=idEstudiante)
    estudiante = get_object_or_404(Estudiante, pk=idEstudiante)
    mensaje = {'estudiante': estudiante}
    return HttpResponse(pagina.render(mensaje, request))

def editar_estudiante(request, idEstudiante):
    pagina = loader.get_template('editar_estudiante.html')
    estudiante = get_object_or_404(Estudiante, pk=idEstudiante)
    if request.method == "GET":
        formulario = EstudianteFormulario(instance=estudiante)
    elif request.method == "POST":
        formulario = EstudianteFormulario(request.POST, instance=estudiante)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')

    mensaje = {'formulario': formulario}

    return HttpResponse(pagina.render(mensaje, request))

def eliminar_estudiante(request, idEstudiante):
    estudiante = get_object_or_404(Estudiante, pk=idEstudiante)
    if estudiante:
        estudiante.delete()
        return redirect('inicio')