from django.shortcuts import render, get_object_or_404
from .cart import Cart
from bikes.models import Bikes
from django.http import JsonResponse


def cart_sumario(request):
    return render(request, 'cart/cart_sumario.html', {})


def cart_adicionar(request):
    print('teste')
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Bikes, id=product_id)
        cart.add(product=product)
        response = JsonResponse({'Product Name': product.nome})
        return response


def cart_deletar(request):
    pass


def cart_atualizar(request):
    pass

