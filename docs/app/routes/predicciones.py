from flask import Flask, request, jsonify, Blueprint
from flask import Blueprint, jsonify, request
from datetime import datetime

from app.services import partidos_service
from app.services.partidos_service import crear_partido
from app.services.partidos_service import eliminar_partido
from app.services.partidos_service import obtener_partido_por_id

partidos_bp = Blueprint("partidos", __name__)

@partidos_bp.route("/partidos/<int:id>/prediccion", methods = ["POST"])
def crear_prediccion(id):
    data = request.json
    partidos_service.crear_prediccion(id, data)
    return {"message": "Prediccion creada exitosamente"}, 201