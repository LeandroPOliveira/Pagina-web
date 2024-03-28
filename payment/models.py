from django.db import models
from django.contrib.auth.models import User
from bikes.models import Produto


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


class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nome_completo = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    endereco_envio = models.TextField(max_length=15000)
    valor_pago = models.DecimalField(max_digits=7, decimal_places=2)
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order - {str(self.id)}'


class ItemPedido(models.Model):
    # Foreign Keys
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    quantidade = models.PositiveBigIntegerField(default=1)
    preco = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f'Item pedido - {str(self.id)}'

