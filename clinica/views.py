from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Paciente, SignosVitales
from .forms import PacienteForm, SignosVitalesForm


# LISTAR PACIENTES
@login_required
def listar_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, "clinica/lista_pacientes.html", {"pacientes": pacientes})


# CREAR PACIENTE
@login_required
def agregar_paciente(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_pacientes")
    else:
        form = PacienteForm()
    return render(request, "clinica/crear_paciente.html", {"form": form})


# EDITAR PACIENTE
@login_required
def editar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    form = PacienteForm(request.POST or None, instance=paciente)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("listar_pacientes")

    return render(request, "clinica/editar_paciente.html", {
        "form": form,
        "paciente": paciente
    })


# ELIMINAR PACIENTE
@login_required
def eliminar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    paciente.delete()
    return redirect("listar_pacientes")


# REGISTRAR SIGNOS
@login_required
def registrar_signos(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)

    if request.method == "POST":
        form = SignosVitalesForm(request.POST)
        if form.is_valid():
            signos = form.save(commit=False)
            signos.paciente = paciente
            signos.registrado_por = request.user
            signos.save()
            return redirect("ver_signos", paciente_id=paciente.id)
    else:
        form = SignosVitalesForm()
    
    return render(request, "clinica/registrar_signos.html", {"form": form, "paciente": paciente})


# EDITAR SIGNOS
@login_required
def editar_signo(request, id):
    signo = get_object_or_404(SignosVitales, id=id)

    if request.method == "POST":
        form = SignosVitalesForm(request.POST, instance=signo)
        if form.is_valid():
            form.save()
            return redirect("ver_signos", paciente_id=signo.paciente.id)
    else:
        form = SignosVitalesForm(instance=signo)

    return render(request, "clinica/editar_signo.html", {"form": form, "signo": signo})


# ELIMINAR SIGNO
@login_required
def eliminar_signo(request, id):
    signo = get_object_or_404(SignosVitales, id=id)
    paciente_id = signo.paciente.id
    signo.delete()
    return redirect("ver_signos", paciente_id=paciente_id)


# VER SIGNOS
@login_required
def ver_signos(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    signos = SignosVitales.objects.filter(paciente=paciente).order_by("-fecha_hora")

    return render(request, "clinica/historial_signos.html", {
        "paciente": paciente,
        "signos": signos
    })
