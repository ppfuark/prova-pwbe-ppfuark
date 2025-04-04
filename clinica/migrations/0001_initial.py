# Generated by Django 5.1.7 on 2025-04-04 19:10

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(5)])),
                ('especialidade', models.CharField(choices=[('CAR', 'Cardiologista'), ('ORT', 'Ortopedista')], max_length=20)),
                ('crm', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(blank=True, default='', max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paciente', models.CharField(max_length=100)),
                ('data', models.DateTimeField()),
                ('status', models.CharField(choices=[('agendado', 'agendado'), ('realizado', 'realizado'), ('cancelado', 'cancelado')], max_length=20)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.medico')),
            ],
        ),
    ]
