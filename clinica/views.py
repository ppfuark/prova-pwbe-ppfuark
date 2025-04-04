from django.shortcuts import redirect, render
from .models import *
from .form import MedicoForm


def listar_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'clinica/listar_medicos.html', {'medicos', medicos})

def criar_consulta(request):
    medicos = Medico.objects.all()

    if request.method == "POST":
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_medicos')
        else:
            form = MedicoForm()

    return render(request, 'clinica/listar_medicos.html', {'medicos', medicos})
        