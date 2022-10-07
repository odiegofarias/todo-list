from django.urls import path
from . import views


app_name = "tarefa"

urlpatterns = [
    path('', views.index, name="index"),
    path('update/<str:pk>', views.updatingTask, name="update"),
    path('delete/<str:pk>', views.deleteTask, name="delete"),
]
