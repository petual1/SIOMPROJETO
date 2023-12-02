from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()

class Medicamento(models.Model):
    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=20, choices=[('Antibiotico','antibiotico'),('Anti Inflamatorio','anti_inflamatorio'),('Analgesico','analgesico')])
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome
