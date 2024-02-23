from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    data_modificacao = models.DateTimeField(User, auto_now=True)
    telefone = models.CharField(max_length=20, blank=True)
    endereco = models.CharField(max_length=200, blank=True)
    cidade = models.CharField(max_length=200, blank=True)
    cep = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.usuario.username


def criar_perfil(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()


post_save.connect(criar_perfil, sender=User)



