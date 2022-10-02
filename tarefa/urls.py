from django.urls import path
from . import views


app_name = "tarefa"

urlpatterns = [
    path('', views.index, name="index"),
    path('apagar/<int:tarefa_id>', views.apagar, name="apagar"),
    path('editar/<int:tarefa_id>', views.editar, name="editar"),
]
