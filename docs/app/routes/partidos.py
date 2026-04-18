from flask import Flask, request, jsonify, Blueprint
from app.services.partidos_service import crear_partido
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