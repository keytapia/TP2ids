from flask import Flask, request, jsonify, Blueprint

from app.db import db
from app.services.partidos_service import crear_partido
from app.services.partidos_service import eliminar_partido
from app.services.partidos_service import obtener_partido_por_id

partidos_bp = Blueprint("partidos", __name__)


# --------------------- CREAR PARTIDO --------------------- #
@partidos_bp.route("/partidos", methods = ['POST'])
def crear_partido():
    dato = request.get_json()
    nuevo_partido = crear_partido(dato)
    if "error" in nuevo_partido:
        error = {
            "errors": [
                {
                    "code": nuevo_partido.get("code.api"),
                    "message": nuevo_partido.get("error"),
                    "level": "error",
                    "descripcion": nuevo_partido.get("description")
                }
            ]
        }
        return jsonify(error)
    return jsonify(nuevo_partido, 201)


# --------------------- BORRAR PARTIDO --------------------- #
@partidos_bp.route("/<int:id>", methods=["DELETE"])
def delete_partido(id):
    try:
        if id <= 0:
            return jsonify({
                "errors": [
                    {
                        "code": 400,
                        "message": "Id invalido",
                        "level": "error",
                        "description": "El id debe ser mayor a 0"
                    }
                ]
            }), 400

        eliminado = eliminar_partido(id)

        if eliminado == 0:
            return jsonify({
                "errors": [
                    {
                        "code": 404,
                        "message": "Partido no encontrado",
                        "level": "error",
                        "description": f"No existe un partido con id {id}"
                    }
                ]
            }), 404

        return "", 204

    except Exception as e:
        db.session.rollback()
        return jsonify({
            "errors": [
                {
                    "code": 500,
                    "message": "Error interno del servidor",
                    "level": "error",
                    "description": str(e)
                }
            ]
        }), 500


# --------------------- OBTENER PARTIDO POR ID --------------------- #
@partidos_bp.route("/<int:id>", methods = ["GET"])
def get_partido(id):
    p = obtener_partido_por_id(id)

    if not p:
        return jsonify({
            "errors": [{
                "code": 404,
                "message": "No se encontró el partido. ",
                "level": "error",
                "description": f"El ID {id} no existe en la base de datos. "
            }]
        }), 404
    
    return jsonify({
        "id": p.id,
        "equipo_local": p.equipo_local,
        "equipo_visitante": p.equipo_visitante,
        "fecha": p.fecha.strftime('%Y-%m-%d') if p.fecha else None,
        "fase": p.fase,
        "resultado": {
            "local": p.goles_local,
            "visitante": p.goles_visitante
        } if p.goles_local is not None else None
    }), 200