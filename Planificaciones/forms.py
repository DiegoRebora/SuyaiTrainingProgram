from django import forms
from .models import Planificacion

class PlanificacionForm(forms.ModelForm):
    class Meta:
        model = Planificacion
        fields = ['semana', 'descripcion', 'fecha_inicio', 'coach', 'comentario']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
        }
