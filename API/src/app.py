
from src.Rutas.UsuarioCRUD import UsuarioCRUD
from src.Rutas.RolCRUD import RolCRUD
from src.database import app
from src.Rutas.RolCRUD import PermisoCRUD


app.register_blueprint(UsuarioCRUD)
app.register_blueprint(RolCRUD)
app.register_blueprint(PermisoCRUD)


if __name__ == '__main__':
    app.run(debug=True)