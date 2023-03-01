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

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

usuario1 = Usuario("Leandro", 'LO', 'tatupeba')
usuario2 = Usuario('Erika', 'EK', 'cozida')
usuario3 = Usuario('Guilherme', 'VE', 'zeca')

usuarios = { usuario1.nickname: usuario1, usuario2.nickname: usuario2, usuario3.nickname: usuario3 }


app = Flask(__name__)
app.secret_key = 'botina'

@app.route('/')
def index():
    return render_template('index.html', bikes=lista, titulo='Coroa36 Bike Store')


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
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
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    proxima_pagina = request.form['proxima']

    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + 'logado com sucesso')
            if proxima_pagina == 'None':
                proxima_pagina = url_for('index')
            return redirect(proxima_pagina)
    else:
        flash('Usuario não encontrado')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso')
    return redirect(url_for('index'))


app.run(debug=True)
