from django.contrib import admin
from estudiantes.models import Carrera, Estudiante, Matricula, Facultad
# Register your models here.

admin.site.register(Carrera)
admin.site.register(Estudiante)
admin.site.register(Matricula)
admin.site.register(Facultad)
