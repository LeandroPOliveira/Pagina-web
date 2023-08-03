from django.shortcuts import render, redirect
from bikes.models import Bikes
from django.contrib import messages


def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    bikes = Bikes.objects.order_by('data_fotografia').filter(publicada=True)
    return render(request, 'bikes/index.html', {'cards': bikes})


