from django.forms import ModelForm
from .models import Tarefa


class TarefaNovaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ["nome"]


class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ["nome", "feita"]