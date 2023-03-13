from flask import Blueprint, request, jsonify
from src.database import db
from src.Modelos.Permiso import Permiso

PermisoCRUD = Blueprint('PermisoCRUD', __name__)

# Obtener todos los permisos
@PermisoCRUD.route('/permisos', methods=['GET'])
def obtener_permisos():
    permisos = Permiso.query.all()
    resultado = []
    for permiso in permisos:
        resultado.append({
            'idpermiso': permiso.idpermiso,
            'nombrepermiso': permiso.nombrepermiso,
            'descripcion': permiso.descripcion,
        })
    return jsonify(resultado)

# Obtener un permiso por ID
@PermisoCRUD.route('/permisos/<int:id>', methods=['GET'])
def obtener_permiso(id):
    permiso = Permiso.query.get(id)
    if permiso:
        resultado = {
            'idpermiso': permiso.idpermiso,
            'nombrepermiso': permiso.nombrepermiso,
            'descripcion': permiso.descripcion
        }
        return jsonify(resultado)
    else:
        return jsonify({'mensaje': 'El permiso no existe'})


# Crear un nuevo permiso
@PermisoCRUD.route('/permisos', methods=['POST'])
def crear_permiso():
    datos = request.json
    permiso = Permiso(
        idpermiso= datos['idpermiso'],
        nombrepermiso=datos['nombrepermiso'],
        descripcion=datos['descripcion']
    )
    db.session.add(permiso)
    db.session.commit()
    return jsonify({'mensaje': 'Permiso creado correctamente'})

# Actualizar un permiso existente
@PermisoCRUD.route('/permisos/<int:id>', methods=['PUT'])
def actualizar_permiso(id):
    permiso = Permiso.query.get(id)
    if permiso:
        datos = request.json
        permiso.nombrepermiso = datos['nombrepermiso']
        permiso.descripcion = datos['descripcion']
        db.session.commit()
        return jsonify({'mensaje': 'Permiso actualizado correctamente'})
    else:
        return jsonify({'mensaje': 'El permiso no existe'})

# Eliminar un permiso existente
@PermisoCRUD.route('/permisos/<int:id>', methods=['DELETE'])
def eliminar_permiso(id):
    permiso = Permiso.query.get(id)
    if permiso:
        db.session.delete(permiso)
        db.session.commit()
        return jsonify({'mensaje': 'Permiso eliminado correctamente'})
    else:
        return jsonify({'mensaje': 'El permiso no existe'})