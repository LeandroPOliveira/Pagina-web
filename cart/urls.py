from django.urls import path
from bikes.views import index, nova_bike, editar_bike, filtro, detalhes_bike

urlpatterns = [
    path('', views.cart_sumario, name='cart_sumario'),
    path('adicionar/', views.cart_adicionar, name='cart_adicionar'),
    path('deletar/', views.cart_deletar, name='cart_deletar'),
    path('atualizar/', views.cart_atualizar, name='cart_atualizar'),
]

