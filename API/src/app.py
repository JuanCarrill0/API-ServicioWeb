
from src.Rutas.UsuarioCRUD import UsuarioCRUD
from src.Rutas.RolCRUD import RolCRUD
from src.database import app
from flask_jwt_extended import JWTManager
from src.Rutas.PermisoCRUD import PermisoCRUD
from src.Autenticación.Autenticacion import Autenticacion

app.register_blueprint(UsuarioCRUD)
app.register_blueprint(RolCRUD)
app.register_blueprint(PermisoCRUD)
app.register_blueprint(Autenticacion)

app.config['JWT_SECRET_KEY'] = 'T4nn3R0x#' # Reemplaza con una clave secreta real
jwt = JWTManager(app)


if __name__ == '__main__':
    app.run(debug=True)