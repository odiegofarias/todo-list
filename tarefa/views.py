from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import TarefaForm, TarefaNovaForm
from .models import Tarefa


def index(request):
    if request.method == "POST":
        form = TarefaNovaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('tarefa:index')
        else:
            tarefas = Tarefa.objects.filter(feita=False).order_by('-id')
            return render(
                request,
                'tarefa/index.html',
                {
                    'form': form,
                    'tarefas': tarefas,
                }
            )
    
    tarefas = Tarefa.objects.all()
    return render(request,'tarefa/index.html', {"tarefas": tarefas})

def editar(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    form = TarefaForm(request.POST, instance=tarefa)

    if form.is_valid():
        form.save()

    return redirect('tarefa:index')
    
    


def apagar(request, tarefa_id):
    if request.method == "POST":
        Tarefa.objects.filter(id=tarefa_id).delete()

    return redirect('tarefa:index')

