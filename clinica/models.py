from django.db import models

ESPECIALIDADES = [
    ('Cardiologia', 'Cardiologia'),
    ('Pediatria', 'Pediatria'),
    ('Dermatologia', 'Dermatologia'),
    ('Ortopedia', 'Ortopedia'),
]

STATUS_CONSULTA = [
    ('agendado', 'Agendado'),
    ('realizado', 'Realizado'),
    ('cancelado', 'Cancelado'),
]

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=50, choices=ESPECIALIDADES)
    crm = models.CharField(max_length=10, unique=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - {self.especialidade}"

class Consulta(models.Model):
    paciente = models.CharField(max_length=100)
    data = models.DateTimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CONSULTA)