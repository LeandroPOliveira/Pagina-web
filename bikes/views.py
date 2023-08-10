from django.shortcuts import render, redirect
from bikes.models import Bikes
from django.contrib import messages
from bikes.forms import BikesForms


def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    bikes = Bikes.objects.order_by('data_fotografia').filter(publicada=True)
    return render(request, 'bikes/index.html', {'cards': bikes})


def nova_bike(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    form = BikesForms()
    for field in form:
        print(field.name)
    if request.method == 'POST':
        form = BikesForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova bicicleta cadastrada!')
            return redirect('index')

    return render(request, 'bikes/nova_bike.html', {'form': form})


def editar_bike(request):
    return render(request, 'bikes/editar_bike.html')
