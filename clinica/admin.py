from django.contrib import admin
from .models import Paciente, SignosVitales

admin.site.register(Paciente)
admin.site.register(SignosVitales)
