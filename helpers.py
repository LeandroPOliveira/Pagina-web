import os
from flask_login import UserMixin
from index import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators, DecimalField


class FormularioBike(FlaskForm):
    nome = StringField('Nome da Bike', [validators.DataRequired(), validators.Length(min=1, max=50)])
    cor = StringField('Cor', [validators.DataRequired(), validators.Length(min=1, max=20)])
    preco = DecimalField('Preco', [validators.DataRequired()])
    salvar = SubmitField('Salvar')


class FormularioUsuario(FlaskForm):
    nickname = StringField('Nickname',  [validators.DataRequired(), validators.Length(min=1, max=8)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=1, max=100)])
    login = SubmitField('Login')

def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo

        return 'capa_padrao.jpg'

def deleta_arquivo(id):
    arquivo = recupera_imagem(id)
    if arquivo != 'capa_padrao.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))


