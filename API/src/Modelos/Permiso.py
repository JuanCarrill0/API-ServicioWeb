from src.database import db

class Permiso(db.Model):
    __tablename__ = 'permiso'
    idpermiso = db.Column(db.Integer, primary_key=True)
    nombrepermiso = db.Column(db.String(15), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False, unique=True)

    def __repr__(self):
        return f'<Permiso {self.nombre}>'