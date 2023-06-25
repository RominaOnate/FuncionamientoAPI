from django.db import models

# Create your models here.
class Carrera(models.Model):
    codigo = models.CharField(max_length=3)
    nombre_carrera = models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        return self.nombre_carrera


class Estudiante(models.Model):
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    cedula = models.CharField(max_length=10)
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1, choices=sexos, null=True)
    email= models.CharField(max_length=50)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)

    def __str__(self):
        return f'id: {self.id} -{self.apellido} -{self.nombre} - {self.carrera}'


class Matricula(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.CharField(max_length=50)
    fecha_matricula = models.DateField()

    def __str__(self):
        return f'{self.estudiante} - {self.curso}'
