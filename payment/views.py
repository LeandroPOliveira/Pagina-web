from django.shortcuts import render
from cart.cart import Cart
from payment.forms import EnderecoForm
from payment.models import Endereco


def checkout(request):
    # Get the cart
    cart = Cart(request)
    cart_produtos = cart.pega_produto
    quantidade = cart.pega_quantidade
    totais = cart.cart_total()

    if request.user.is_authenticated:
        # Checkout as logged in user
        # Shipping User
        shipping_user = Endereco.objects.get(usuario__id=request.user.id)
        # Shipping Form
        shipping_form = EnderecoForm(request.POST or None, instance=shipping_user)
        return render(request, "checkout.html",
                      {"cart_produtos": cart_produtos, "quantidade": quantidade, "totais": totais,
                       "shipping_form": shipping_form})
    else:
        # Checkout as guest
        shipping_form = EnderecoForm(request.POST or None)
        return render(request, "checkout.html",
                      {"cart_produto": cart_produto, "quantidade": quantidade, "totais": totais,
                       "shipping_form": shipping_form})


def pagamento_sucesso(request):
    return render(request, 'pagamento_sucesso.html', {})
