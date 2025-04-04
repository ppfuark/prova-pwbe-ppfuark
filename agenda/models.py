from django.db import models

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    duracao = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)

class Agendamento(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data_hora = models.DateField()
    cliente_nome = models.CharField(max_length=100)
    cliente_email = models.EmailField()