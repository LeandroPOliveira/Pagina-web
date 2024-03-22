from django.contrib import admin
from .models import Endereco, Pedido, ItemPedido


# Register the model on the admin section thing
admin.site.register(Endereco)
admin.site.register(Pedido)
admin.site.register(ItemPedido)
