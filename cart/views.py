from django.shortcuts import render, get_object_or_404
from .cart import Cart
from bikes.models import Bikes
from django.http import JsonResponse
from django.contrib import messages


def cart_sumario(request):
    return render(request, 'cart_sumario.html', {})


def cart_adicionar(request):
    # Get the cart
    cart = Cart(request)
    # test for POST
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        print(product_id)
        # lookup product in DB
        product = get_object_or_404(Product, id=product_id)

        # Save to session
        cart.add(product=product)

        # Get Cart Quantity
        cart_quantity = cart.__len__()

        # Return resonse
        # response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'qty': cart_quantity})
        messages.success(request, ("Product Added To Cart..."))
        return response


def cart_deletar(request):
    pass


def cart_atualizar(request):
    pass

