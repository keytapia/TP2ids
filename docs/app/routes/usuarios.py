from flask import Flask, request, jsonify, Blueprint
from app.services.usurios_service import crear_usuario
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








