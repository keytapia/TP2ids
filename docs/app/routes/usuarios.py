from flask import Flask, request, jsonify, Blueprint
from app.services.usurios_service import crear_usuario, obtener_usuario_por_id
from app.db import db

usuarios_bp = Blueprint("usuarios", __name__)


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
