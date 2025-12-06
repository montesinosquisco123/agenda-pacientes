from django import forms
from .models import Paciente, SignosVitales

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'rut', 'habitacion', 'edad', 'alergias']


class SignosVitalesForm(forms.ModelForm):
    class Meta:
        model = SignosVitales
        fields = [
            'presion_arterial',
            'pam',
            'frecuencia_cardiaca',
            'frecuencia_respiratoria',
            'spo2',
            'oxigeno_apoyo'
        ]
