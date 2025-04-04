import datetime
from django.db import models
from django.core.validators import MinLengthValidator
from django.forms import ValidationError
from django.utils.translation import ugettext_lazy

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
    nome = models.CharField(validators=[MinLengthValidator(5)] , max_length=100)
    especialidade = models.CharField(max_length=20, choices=choices)
    crm = models.CharField(max_length=20, unique=True)  
    email = models.EmailField(blank=True, null=True, default="")
    
    def __str__(self):
        return self.nome

class Consulta(models.Model):
    paciente = models.CharField(max_length=100)
    data = models.DateTimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=choicesStatus)      

    def clean_date(self):
        data = self.cleaned_data['data']

        if data < datetime.date.today():
            raise ValidationError(ugettext_lazy('Data no Passado')) 
        
        return data
    
    def __str__(self):
        return self.paciente