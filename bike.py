from flask import Flask, render_template, request, redirect

class Bicicleta():
    def __init__(self, nome, foto, cor, preco):
        self.nome = nome
        self.foto = foto
        self.cor = cor
        self.preco = preco

bike1 = Bicicleta('Epic Pro', 'static/img/branca.webp', 'Branca', 'R$ 79.000,00')
bike2 = Bicicleta('Epic S-Works', 'static/img/works.webp', 'Verde', 'R$ 114.900,00')
lista = [bike1, bike2]

app = Flask(__name__)


@app.route('/home')
def dados():
    return render_template('index.html', bikes=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    imagem = 'static/img/' + request.form['imagem']
    cor = request.form['cor']
    preco = request.form['preco']
    nova_bike = Bicicleta(nome, imagem, cor, preco)
    print(imagem)
    lista.append(nova_bike)
    return redirect('/home')

app.run()
