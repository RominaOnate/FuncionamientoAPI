from rest_framework import serializers

from estudiantes.models import Estudiante, Carrera, Facultad


class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = ['nombre_carrera']

class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        fields = ['nombre_facultad']

class EstudianteSerializer(serializers.HyperlinkedModelSerializer):
    carrera = CarreraSerializer()
    facultad = FacultadSerializer()
    class Meta:
        model = Estudiante
        fields = ['cedula', 'apellido', 'nombre', 'sexo', 'email', 'carrera', 'facultad', 'vigencia']