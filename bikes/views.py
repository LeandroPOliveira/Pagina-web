from django.shortcuts import render, redirect, get_object_or_404
from bikes.models import Produto
from django.contrib import messages
from bikes.forms import ProdutoForm
import datetime


def index(request):
    # if not request.user.is_authenticated:
    #     messages.error(request, 'Usuário não logado')
    #     return redirect('login')

    bikes = Produto.objects.order_by('data_fotografia').filter(publicada=True)
    titulo = 'Trokabike'
    ano = datetime.date.today().year
    return render(request, 'bikes/index.html', {'cards': bikes, 'titulo': titulo, 'ano': ano})


def editar_bike(request):
    return render(request, 'bikes/editar_bike.html')


def filtro(request, categoria):
    bikes = Produto.objects.order_by('data_fotografia').filter(publicada=True, categoria=categoria)
    return render(request, 'bikes/index.html', {'cards': bikes})


def detalhes_bike(request, bike_id):
    bike = get_object_or_404(Produto, pk=bike_id)
    return render(request, 'bikes/detalhes_bike.html', {'bike': bike})


