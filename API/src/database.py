from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
<<<<<<< HEAD
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://NombreUsuario:Contraseña.@localhost/NombreBaseDeDatos'
=======

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://NombreUsuario:Contraseña@localhost/NombreBaseDatos'
>>>>>>> main
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()
