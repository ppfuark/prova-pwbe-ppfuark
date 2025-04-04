from django.db import models
from django.core.validators import MinLengthValidator

choices = [
    ("CAR", "Cardiologista"),
    ("ORT", "Ortopedista")
]
choicesStatus = [
    ('agendado', 'agendado'), 
    ('realizado', 'realizado'), 
    ('cancelado', 'cancelado')
]

class Medico(models.Model):
    nome = models.CharField(max_length=50,  validators=[MinLengthValidator(5)])
    especialidade = models.CharField(choices=choices, max_length=50)
    crm = models.CharField(unique=True, max_length=8, validators=[MinLengthValidator(8)])
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    paciente = models.CharField(max_length=50)
    data = models.DateTimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='+')
    status = models.CharField(choices=choicesStatus, max_length=50)

    def __str__(self):
        return self.paciente