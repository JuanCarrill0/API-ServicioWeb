
from API.src.Rutas.UsuarioCRUD import UsuarioCRUD
from API.src.Rutas.RolCRUD import RolCRUD
from API.src.Rutas.PermisoCRUD import PermisoCRUD
from API.src.database import app


app.register_blueprint(UsuarioCRUD)
app.register_blueprint(RolCRUD)
app.register_blueprint(PermisoCRUD)

if __name__ == '__main__':
    app.run(debug=True)