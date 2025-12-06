from django.db import models
from django.contrib.auth.models import User

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    habitacion = models.CharField(max_length=10)
    edad = models.IntegerField()
    alergias = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} - Habitación {self.habitacion}"


class SignosVitales(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    presion_arterial = models.CharField(max_length=20)
    pam = models.CharField(max_length=10)
    frecuencia_cardiaca = models.IntegerField()
    frecuencia_respiratoria = models.IntegerField()
    spo2 = models.IntegerField()
    oxigeno_apoyo = models.CharField(max_length=50, blank=True)
    registrado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Signos de {self.paciente.nombre} - {self.fecha_hora}"
