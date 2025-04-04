from django.shortcuts import render, get_object_or_404, redirect
from .models import Medico, Consulta
from .form import ConsultaForm

def listar_medicos(request):
    especialidade = request.GET.get('especialidade')
    if especialidade:
        medicos = Medico.objects.filter(especialidade=especialidade)
    else:
        medicos = Medico.objects.all()
    return render(request, 'listar_medicos.html', {'medicos': medicos})

def criar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/medicos/')
    else:
        form = ConsultaForm()
    return render(request, 'form_consulta.html', {'form': form})

def detalhes_consulta(request, id):
    consulta = get_object_or_404(Consulta, id=id)
    return render(request, 'detalhes_consulta.html', {'consulta': consulta})