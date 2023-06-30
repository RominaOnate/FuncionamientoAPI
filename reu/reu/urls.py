"""
URL configuration for reu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import mostrar_estudiantes
from estudiantes.views import agregar_estudiante, ver_estudiante, editar_estudiante, eliminar_estudiante, \
    generar_reporte

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mostrar_estudiantes, name='inicio'),
    path('agregar_estudiante/', agregar_estudiante),
    path('ver_estudiante/<int:idEstudiante>', ver_estudiante),
    path('editar_estudiante/<int:idEstudiante>', editar_estudiante),
    path('eliminar_estudiante/<int:idEstudiante>', eliminar_estudiante),
    path('generar_reporte/', generar_reporte),

]
