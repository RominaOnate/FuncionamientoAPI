from django.forms import ModelForm, EmailInput
from estudiantes.models import Estudiante

class EstudianteFormulario(ModelForm):
    class Meta:
        model = Estudiante
        fields = ('cedula', 'apellido', 'nombre', 'sexo', 'email', 'carrera', 'vigencia')
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }