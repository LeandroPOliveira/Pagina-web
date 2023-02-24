from flask import Flask, render_template, request, redirect, session, flash, url_for


class Bicicleta:
    def __init__(self, nome, foto, cor, preco):
        self.nome = nome
        self.foto = foto
        self.cor = cor
        self.preco = preco


bike1 = Bicicleta('Epic Pro', 'static/img/branca.webp', 'Branca', 'R$ 79.000,00')
bike2 = Bicicleta('Epic S-Works', 'static/img/works.webp', 'Verde', 'R$ 114.900,00')
lista = [bike1, bike2]

app = Flask(__name__)
app.secret_key = 'botina'

@app.route('/')
def index():
    return render_template(url_for('index'), bikes=lista, titulo='Coroa36 Bike Store')


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=novo')
    return render_template('novo.html', titulo='Nova Bike')


@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    imagem = 'static/img/' + request.form['imagem']
    cor = request.form['cor']
    preco = request.form['preco']
    nova_bike = Bicicleta(nome, imagem, cor, preco)
    print(imagem)
    lista.append(nova_bike)
    return redirect('/')


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if 'tatupeba' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + 'logado com sucesso')
        proxima_pagina = request.form['proxima']
        return redirect(f'/{proxima_pagina}')
    else:
        flash('Usuario não encontrado')
        return redirect('/login')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso')
    return redirect('/')


app.run(debug=True)
