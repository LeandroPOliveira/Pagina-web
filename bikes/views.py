from django.shortcuts import render, redirect, get_object_or_404
from bikes.models import Bikes
from django.contrib import messages
from bikes.forms import BikesForms


def index(request):
    # if not request.user.is_authenticated:
    #     messages.error(request, 'Usuário não logado')
    #     return redirect('login')

    bikes = Bikes.objects.order_by('data_fotografia').filter(publicada=True)
    titulo = 'Trokabike'
    return render(request, 'bikes/index.html', {'cards': bikes, 'titulo': titulo})


def nova_bike(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    form = BikesForms()
    if request.method == 'POST':
        form = BikesForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova bicicleta cadastrada!')
            return redirect('index')
        else:
            print(form.errors.as_data())

    return render(request, 'bikes/nova_bike.html', {'form': form})


def editar_bike(request):
    return render(request, 'bikes/editar_bike.html')


def filtro(request, categoria):
    bikes = Bikes.objects.order_by('data_fotografia').filter(publicada=True, categoria=categoria)
    return render(request, 'bikes/index.html', {'cards': bikes})


def detalhes_bike(request, bike_id):
    bike = get_object_or_404(Bikes, pk=bike_id)
    return render(request, 'bikes/detalhes_bike.html', {'bike': bike})


