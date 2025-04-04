from django.urls import path
from . import views 

urlpatterns = [
    path("/medicos/", views.listar_medicos, name='listar_medicos'),
    path("/consultas/nova/", views.listar_medicos, name='listar_medicos'),
    path("/consultas/<int:id>/", views.listar_medicos, name='listar_medicos'),
]