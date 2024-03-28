from django.shortcuts import render, get_object_or_404
from .cart import Cart
from bikes.models import Produto
from django.http import JsonResponse
from django.contrib import messages


def cart_sumario(request):
    cart = Cart(request)
    cart_produtos = cart.pega_produto
    quantidade = cart.pega_quantidade
    totais = cart.cart_total()
    return render(request, 'cart_sumario.html', {'cart_produtos': cart_produtos, 'quantidade': quantidade, 'totais': totais})


def cart_adicionar(request):
    # Get the cart
    cart = Cart(request)
    # test for POST
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        # lookup product in DB
        product = get_object_or_404(Produto, id=product_id)

        # Save to session
        cart.adicionar(product=product, quantity=product_qty)

        # Get Cart Quantity
        cart_quantity = cart.__len__()

        # Return resonse
        # response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'qty': cart_quantity})
        messages.success(request, ("Produto adicionado ao carrinho!"))
        return response


def cart_deletar(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.deletar(produto=product_id)
        response = JsonResponse({'product': product_id})
        messages.success(request, ("Item removido do carrinho!"))
        return response


def cart_atualizar(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':

        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.atualizar(produto=product_id, quantidade=product_qty)
        response = JsonResponse({'qty': product_qty})
        messages.success(request, ("Seu carrinho foi atualizado!"))
        return response
        # return redirect('cart_sumario')

