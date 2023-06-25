from django.contrib import admin
from estudiantes.models import Carrera, Estudiante, Matricula
# Register your models here.

admin.site.register(Carrera)
admin.site.register(Estudiante)
admin.site.register(Matricula)

