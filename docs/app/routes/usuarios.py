from flask import Blueprint, jsonify, request

from app.db import db
from app.services.usuarios_service import crear_usuario
from app.services.usuarios_service import eliminar_usuario
from app.services.usuarios_service import obtener_usuario_por_id

usuarios_bp = Blueprint("usuarios", __name__)


# --------------------- CREAR USUARIO --------------------- #
@usuarios_bp.route("/usuarios", methods=["POST"])
def crear_usuario():
    dato = request.get_json()
    nuevo_usuario = crear_usuario(dato)
    if "error" in nuevo_usuario:
        error = {
            "errors": [
                {
                    "code": nuevo_usuario.get("code.api"),
                    "message": crear_usuario.get("error"),
                    "level": "error",
                    "descripcion": crear_usuario.get("description")
                }
            ]
        }
        return jsonify(error)
    return jsonify(nuevo_usuario, 201)


# --------------------- BORRAR USUARIO --------------------- #
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


# --------------------- OBTENER USUARIO POR ID --------------------- #
@usuarios_bp.route("/<int:id>", methods=["GET"])
def get_usuario(id):
    u = obtener_usuario_por_id(id)

    if not u: 
        return jsonify({ 
            "errors": [{ 
                "code": 404, 
                "message": "Usuario no encontrado",
                "level": "error",
                "description": f"No existe un usuario con el ID {id}." 
            }] 
        }), 404

    return jsonify({ 
        "id": u.id, 
        "nombre": u.nombre,
        "email": u.email
    }), 200