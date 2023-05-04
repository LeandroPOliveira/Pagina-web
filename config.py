import os

SECRET_KEY = 'botina'

# postgres://bikedata_user:y8Ra0f445ZjEREBE5hrEWyBMGZ5m0U8d@dpg-ch8rb6rhp8u0vhfplnk0-a.oregon-postgres.render.com/bikedata
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
# '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
# SGBD= 'mysql+mysqlconnector',
# servidor = 'localhost',
# usuario = 'root',
# senha = os.environ['senha'],
# database = 'catalogo')

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'