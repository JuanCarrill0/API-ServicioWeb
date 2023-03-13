
from src.Rutas.UsuarioCRUD import UsuarioCRUD
from src.database import app


app.register_blueprint(UsuarioCRUD)

if __name__ == '__main__':
    app.run(debug=True)