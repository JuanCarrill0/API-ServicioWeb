
from src.Rutas.UsuarioCRUD import UsuarioCRUD
from src.Rutas.RolCRUD import RolCRUD
from src.database import app


app.register_blueprint(UsuarioCRUD)
app.register_blueprint(RolCRUD)


if __name__ == '__main__':
    app.run(debug=True)