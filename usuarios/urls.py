# usuarios > urls.py

from django.urls import path
from usuarios.views import login, cadastro, logout, perfil, nova_senha

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('perfil', perfil, name='perfil'),
    path('nova-senha', nova_senha, name='nova_senha'),
    path('logout', logout, name='logout'),
]