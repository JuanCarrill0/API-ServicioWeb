from flask import Flask
from src.Rutas.UsuarioCRUD import UsuarioCRUD
from src.database import db

app_principal = Flask(__name__)
app_principal.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Juancarrillo09@localhost/ServicioWeb'
app_principal.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app_principal)

with app_principal.app_context():
    db.create_all()

app_principal.register_blueprint(UsuarioCRUD)

if __name__ == '__main__':
    app_principal.run(debug=True)