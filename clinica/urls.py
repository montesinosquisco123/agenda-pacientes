from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar_pacientes, name="listar_pacientes"),
    path("crear/", views.agregar_paciente, name="crear_paciente"),
    path("editar/<int:id>/", views.editar_paciente, name="editar_paciente"),
    path("eliminar/<int:id>/", views.eliminar_paciente, name="eliminar_paciente"),

    # SIGNOS
    path("paciente/<int:paciente_id>/signos/", views.ver_signos, name="ver_signos"),
    path("paciente/<int:paciente_id>/registrar/", views.registrar_signos, name="registrar_signos"),

    path("signos/editar/<int:id>/", views.editar_signo, name="editar_signo"),
    path("signos/eliminar/<int:id>/", views.eliminar_signo, name="eliminar_signo"),
]
