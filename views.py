from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from index import app, db
from models import Bikes, Usuarios
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
    cor = request.form['cor']
    preco = request.form['preco']

    bike = Bikes.query.filter_by(nome=nome).first()

    if bike:
        flash('Bike já cadastrada!')
        return redirect(url_for('index'))

    nova_bike = Bikes(nome=nome, cor=cor, preco=preco)
    db.session.add(nova_bike)
    db.session.commit()

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    arquivo.save(f'{upload_path}/capa{nova_bike.id}.jpg')


    return redirect(url_for('index'))


@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar')))
    bike = Bikes.query.filter_by(id=id).first()
    return render_template('editar.html', titulo='Editando Bike', bike=bike)


@app.route('/atualizar', methods=['POST', ])
def atualizar():
    bike = Bikes.query.filter_by(id=request.form['id']).first()
    bike.nome = request.form['nome']
    bike.cor = request.form['cor']
    bike.preco = request.form['preco']

    db.session.add(bike)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))

    Bikes.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Jogo deletado com sucesso!')

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

@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)