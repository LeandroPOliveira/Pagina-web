from index import db


class Bikes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    cor = db.Column(db.String(40), nullable=False)
    preco = db.Column(db.Numeric(20, 2), nullable=False)
    ano = db.Column(db.String(40), nullable=False)
    descricao = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome


class Usuarios(db.Model):
    nickname = db.Column(db.String(8), primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name