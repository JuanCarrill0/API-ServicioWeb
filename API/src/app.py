
from API.src.Rutas.UsuarioCRUD import UsuarioCRUD
from API.src.database import app


app.register_blueprint(UsuarioCRUD)

if __name__ == '__main__':
    app.run(debug=True)