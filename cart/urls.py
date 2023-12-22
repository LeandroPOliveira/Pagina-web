from django.urls import path
from cart.views import cart_sumario, cart_adicionar, cart_deletar, cart_atualizar

urlpatterns = [
    path('sumario', cart_sumario, name='cart_sumario'),
    path('adicionar/', cart_adicionar, name='cart_adicionar'),
    path('deletar/', cart_deletar, name='cart_deletar'),
    path('atualizar/', cart_atualizar, name='cart_atualizar'),
]

