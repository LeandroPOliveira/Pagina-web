from django.urls import path
from . import views

urlpatterns = [
    path('sumario', views.cart_sumario, name='cart_sumario'),
    path('adicionar', views.cart_adicionar, name='cart_adicionar'),
    path('deletar/', views.cart_deletar, name='cart_deletar'),
    path('atualizar/', views.cart_atualizar, name='cart_atualizar'),
]

