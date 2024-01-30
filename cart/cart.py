from bikes.models import Bikes


class Cart:
    def __init__(self, request):
        self.session = request.session

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

        retorno = self.cart
        return retorno

    def deletar(self, produto):
        produto_id = str(produto)
        if produto_id in self.cart:
            del self.cart[produto_id]

        self.session.modified = True

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


