from flask import Blueprint, jsonify, request

from TP2ids.docs.app.services import usuarios_service
from app.db import db
from app.services.usuarios_service import crear_usuario
from app.services.usuarios_service import eliminar_usuario
from app.services.usuarios_service import obtener_usuario_por_id

usuarios_bp = Blueprint("usuarios", __name__)

# ---------------------- LISTA USUARIOS --------------------- #
@usuarios_bp.route("/usuarios", methods=["GET"])
def lista_usuarios():
    usuarios = usuarios_service.obtener_lista_usuarios()
    return jsonify(usuarios)

# --------------------- CREAR USUARIO --------------------- #
@usuarios_bp.route("/usuarios", methods=["POST"])
def crear_usuario():
    data = request.json
    usuarios_service.crear_usuario(data)
    return jsonify({"message": "Usuario creado exitosamente"}), 200

# ---------------------- BUSCA USUARIO POR ID --------------------- # 
@usuarios_bp.route("/usuarios/<int:id>", methods=["GET"])
def usuario_por_id(id):
    usuario = usuarios_service.usuario_por_id(id)
    if usuario is None:
        return {"Error": "Usuario no encontrado"}, 404
    return jsonify(usuario)

#---------------------- ACTUALIZAR USUARIO --------------------- #
@usuarios_bp.route("/usuarios/<int:id>", methods=["PUT"])
def actualizar_usuario(id):
    data = request.json
    usuarios_service.actualizar_usuario(id, data)
    return {"message": "Usuario actualizado exitosamente"}, 200

# --------------------- BORRAR USUARIO --------------------- # 
@usuarios_bp.route("/<int:id>", methods=["DELETE"])
def delete_usuario(id):
    if id <= 0:
        return {"error": "ID invalido"}, 400
    resultado = usuarios_service.delete_usuario(id)

    if resultado is False:
        return {"error": "Usuario no encontrado"}, 404

    if resultado is None:
        return {"error": "Error al eliminar el usuario"}, 500
    return {"message": "Usuario eliminado exitosamente"}, 200