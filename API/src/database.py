from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Juancarrillo09@localhost/ServicioWeb'
db = SQLAlchemy(app)
