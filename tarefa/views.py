from django.shortcuts import render, redirect
from .forms import TarefaForm
from .models import Tarefa


def index(request):
    tarefas = Tarefa.objects.all()

    form = TarefaForm()

    if request.method == "POST":
        form = TarefaForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('/')
    
    context = {'tarefas': tarefas, 'form': form}

    return render(request, 'tarefa/list.html', context)


def updatingTask(request, pk):
    tarefa = Tarefa.objects.get(id=pk)

    form = TarefaForm(instance=tarefa)

    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}

    return render(request, 'tarefa/update.html', context)


def deleteTask(request, pk):
    item = Tarefa.objects.get(id=pk)

    if request.method == "POST":
        item.delete()
        return redirect('/')

    context = {'item': item}

    return render(request, 'tarefa/delete.html', context)