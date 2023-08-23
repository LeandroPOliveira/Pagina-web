from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Bikes(models.Model):

    OPCOES_CATEGORIA = [
        ('MOUNTAIN', "Mountain"),
        ('ROAD', 'Road'),
        ('GRAVEL', 'Gravel'),
    ]

    nome = models.CharField(max_length=50, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    cor = models.CharField(max_length=40)
    preco = models.DecimalField(max_digits=9, decimal_places=2)
    ano = models.CharField(max_length=40)
    descricao = models.CharField(max_length=300)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d", blank=True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    usuarios = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=False, related_name='user', )

    def __str__(self):
        return self.nome

