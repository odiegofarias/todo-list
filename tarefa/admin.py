from django.contrib import admin
from .models import Tarefa


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'data_criacao', 'feita')
    list_display_links = ('nome',)
    list_editable = ('feita',)
