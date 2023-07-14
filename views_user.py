from index import app, login_manager
from flask import render_template, request, redirect, session, flash, url_for
from helpers import FormularioUsuario
from models import Usuarios
from flask_bcrypt import check_password_hash
from flask_login import login_user, current_user, login_required, logout_user


@login_manager.user_loader
def load_user(usuarios_id):
    return Usuarios.query.get(int(usuarios_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    proxima = request.args.get('proxima')
    form = FormularioUsuario()
    if form.validate_on_submit():
        usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
        if usuario:
            if check_password_hash(usuario.senha, form.senha.data):
                login_user(usuario)
                flash(usuario.nickname + 'logado com sucesso')
                return redirect(url_for('index'))
            else:
                flash('Senha incorreta! Tente novamente.')
        else:
            flash('Usuário não cadastrado. Tente novamente.')

    return render_template('login.html', proxima=proxima, form=form)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('Logout efetuado com sucesso')
    return redirect(url_for('index'))