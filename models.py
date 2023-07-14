from index import db
from flask_login import UserMixin

class Bikes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    cor = db.Column(db.String(40), nullable=False)
    preco = db.Column(db.Numeric(20, 2), nullable=False)
    ano = db.Column(db.String(40), nullable=False)
    descricao = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome


class Usuarios(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nickname = db.Column(db.String(20))
    nome = db.Column(db.String(30), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome