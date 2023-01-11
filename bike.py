from flask import Flask, render_template

class Bicicleta():
    def __init__(self, nome, foto, cor, preco):
        self.nome = nome
        self.foto = foto
        self.cor = cor
        self.preco = preco

app = Flask(__name__)


@app.route('/home')
def dados():
    bike1 = Bicicleta('Epic Pro', 'static/img/branca.webp', 'Branca', 'R$ 79.000,00')
    bike2 = Bicicleta('Epic S-Works', 'static/img/works.webp', 'Verde', 'R$ 114.900,00')
    return render_template('index.html', bikes=[bike1, bike2])


app.run()
