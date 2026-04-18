from flask import Flask, request, jsonify, Blueprint
from app.services.partidos_service import crear_partido, obtener_partido_por_id
from app.db import db


partidos_bp = Blueprint("partidos", __name__)

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