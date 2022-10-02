from django.db import models


class Tarefa(models.Model):
    nome = models.CharField(max_length=65)
    feita = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nome

    class Meta:
        ordering = ['-data_criacao']
