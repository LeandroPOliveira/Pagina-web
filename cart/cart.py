from bikes.models import Bikes
from usuarios.models import Profile


class Cart:
    def __init__(self, request):
        self.session = request.session
        self.request = request

        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def adicionar(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(usuario__id=self.request.user.id)

            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            current_user.update(old_cart=carty)

    def db_add(self, product, quantity):
        product_id = str(product)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(usuario__id=self.request.user.id)

            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            current_user.update(old_cart=carty)

    def __len__(self):
        return len(self.cart)

    def pega_produto(self):
        produtos_id = self.cart.keys()
        produtos = Bikes.objects.filter(id__in=produtos_id)

        return produtos

    def pega_quantidade(self):
        quantidade = self.cart
        return quantidade

    def atualizar(self, produto, quantidade):
        produto_id = str(produto)
        produto_qtd = int(quantidade)

        carrinho = self.cart

        carrinho[produto_id] = produto_qtd

        self.session.modified = True
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(usuario__id=self.request.user.id)

            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            current_user.update(old_cart=carty)

        retorno = self.cart
        return retorno

    def deletar(self, produto):
        produto_id = str(produto)
        if produto_id in self.cart:
            del self.cart[produto_id]

        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(usuario__id=self.request.user.id)

            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            current_user.update(old_cart=carty)

    def cart_total(self):
        produtos_id = self.cart.keys()
        products = Bikes.objects.filter(id__in=produtos_id)
        quantidade = self.cart
        total = 0
        for key, value in quantidade.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    total = total + (product.preco * value)

        return total


