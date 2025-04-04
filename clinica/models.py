from django.db import models

choices = [
    ("CAR", "Cardiologista"),
    ("ORT", "Ortopedista")
]


class Medico(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=20, choices=choices)
    crm = models.CharField(unique=True)
    email = models.EmailField(null=True, default="")

class Consulta(models.Model):
    paciente = models.CharField(max_length=100)
    data = models.DateTimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    status = models.CharField(choices=['agendado', 'realizado', 'cancelado'])       