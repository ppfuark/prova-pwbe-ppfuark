from django.db import models

choices = [
    ("CAR", "Cardiologista"),
    ("ORT", "Ortopedista")
]
choicesStatus = [
    ("agendado", "agendado"),
    ("realizado", "realizado"),
    ("cancelado", "cancelado")
]


class Medico(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=20, choices=choices)
    crm = models.CharField(max_length=20, unique=True)
    email = models.EmailField(null=True, default="")

class Consulta(models.Model):
    paciente = models.CharField(max_length=100)
    data = models.DateTimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=choicesStatus)       