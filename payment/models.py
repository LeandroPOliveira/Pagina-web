from django.db import models
from django.contrib.auth.models import User


class Endereco(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    email_envio = models.CharField(max_length=255)
    endereco_envio = models.CharField(max_length=255)
    endereco_envio2 = models.CharField(max_length=255)
    cidade_envio = models.CharField(max_length=255)
    estado_envio = models.CharField(max_length=255, null=True, blank=True)
    cep_envio = models.CharField(max_length=255, null=True, blank=True)
    pais_envio = models.CharField(max_length=255)

    # Don't pluralize address
    class Meta:
        verbose_name_plural = "Endereço Entrega"

    def __str__(self):
        return f'Endereço Entrega - {str(self.id)}'
