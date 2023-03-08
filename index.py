import os

from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'botina'



app.config['SQLALCHEMY_DATABASE_URI'] = \
'{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
SGBD= 'mysql+mysqlconnector',
servidor = 'localhost',
usuario = 'root',
senha = os.environ['senha'],
database = 'catalogo')

db = SQLAlchemy(app)
class Bikes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    cor = db.Column(db.String(40), nullable=False)
    preco = db.Column(db.Numeric(20, 2), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


class Usuarios(db.Model):
    nickname = db.Column(db.String(8), primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


@app.route('/')
def index():
    lista = Bikes.query.order_by(Bikes.id)
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

    bike = Bikes.query.filter_by(nome=nome).first()

    if bike:
        flash('Bike já cadastrada!')
        return redirect(url_for('index'))

    nova_bike = Bikes(nome=nome, cor=cor, preco=preco)
    db.session.add(nova_bike)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    usuario = Usuarios.query.filter_by(nickname=request.form['usuario']).first()
    proxima_pagina = request.form['proxima']
    if usuario:
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
