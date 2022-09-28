from django.urls import path
from . import views


app_name = "tarefa"

urlpatterns = [
    path('', views.index, name="index"),
]
