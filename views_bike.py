from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from index import app, db
from models import Bikes
from helpers import recupera_imagem, deleta_arquivo, FormularioBike
import time

@app.route('/')
def index():
    lista = Bikes.query.order_by(Bikes.id)
    print(lista)
    return render_template('index.html', bikes=lista, titulo='Coroa36 Bike Store')


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    form = FormularioBike()
    return render_template('novo.html', titulo='Nova Bike', form=form)


@app.route('/criar', methods=['POST', ])
def criar():
    form = FormularioBike(request.form)

    if not form.validate_on_submit():
        return redirect(url_for('novo'))


    nome = form.nome.data
    cor = form.cor.data
    preco = form.preco.data

    bike = Bikes.query.filter_by(nome=nome).first()

    if bike:
        flash('Bike já cadastrada!')
        return redirect(url_for('index'))

    nova_bike = Bikes(nome=nome, cor=cor, preco=preco)
    db.session.add(nova_bike)
    db.session.commit()

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    # arquivo.save(f'{upload_path}/capa{nova_bike.id}-{timestamp}.jpg')
    arquivo.save(f'{upload_path}/capa{nova_bike.id}.jpg')

    return redirect(url_for('index'))


@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar', id=id)))
    bike = Bikes.query.filter_by(id=id).first()
    print(bike)
    form = FormularioBike()
    form.nome.data = bike.nome
    form.cor.data = bike.cor
    form.preco.data = bike.preco

    capa_bike = recupera_imagem(id)
    return render_template('editar.html', titulo='Editando Bike', id=id, capa_bike=capa_bike, form=form)


@app.route('/atualizar', methods=['POST', ])
def atualizar():
    form = FormularioBike(request.form)

    if form.validate_on_submit():
        bike = Bikes.query.filter_by(id=request.form['id']).first()
        bike.nome = form.nome.data
        bike.cor = form.cor.data
        bike.preco = form.preco.data

        db.session.add(bike)
        db.session.commit()

        arquivo = request.files['arquivo']
        upload_path = app.config['UPLOAD_PATH']
        timestamp = time.time()
        deleta_arquivo(bike.id)
        arquivo.save(f'{upload_path}/capa{bike.id}-{timestamp}.jpg')

    return redirect(url_for('index'))


@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))

    Bikes.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Jogo deletado com sucesso!')

    return redirect(url_for('index'))




@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)

