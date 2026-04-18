from flask import Blueprint, jsonify
from app.services.usuarios_service import eliminar_usuario
from app.db import db

usuarios_bp = Blueprint("usuarios", _name_)

#DELETE
@usuarios_bp.route("/<int:id>", methods=["DELETE"])
def delete_usuario(id):
    try:
        if id <= 0:
            error = {
                "errors": [
                    {
                        "code": 400,
                        "message": "Id invalido",
                        "level": "error",
                        "description": "El id debe ser mayor a 0"
                    }
                ]
            }
            return jsonify(error), 400

        eliminado = eliminar_usuario(id)

        if eliminado == 0:
            error = {
                "errors": [
                    {
                        "code": 404,
                        "message": "Usuario no encontrado",
                        "level": "error",
                        "description": f"No existe un usuario con id {id}"
                    }
                ]
            }
            return jsonify(error), 404

        return "", 204

    except Exception as e:
        db.session.rollback()
        error = {
            "errors": [
                {
                    "code": 500,
                    "message": "Error interno del servidor",
                    "level": "error",
                    "description": str(e)
                }
            ]
        }
        return jsonify(error), 500
