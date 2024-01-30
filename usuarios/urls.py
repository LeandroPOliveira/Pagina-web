# usuarios > urls.py

from django.urls import path
from usuarios.views import login, cadastro, logout, perfil

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('perfil', perfil, name='perfil'),
    path('logout', logout, name='logout'),
]