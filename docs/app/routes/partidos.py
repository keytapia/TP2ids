from flask import Flask, request, jsonify, Blueprint
from flask import Blueprint, jsonify, request
from datetime import datetime

from app.db import db
from app.services import partidos_service
from app.services.partidos_service import crear_partido
from app.services.partidos_service import eliminar_partido
from app.services.partidos_service import obtener_partido_por_id

partidos_bp = Blueprint("partidos", __name__)

#---------------------  LISTA PARTIDOS --------------------- #
@partidos_bp.route("/partidos", methods = ["GET"])
def lista_partidos():
    partidos = partidos_service.obtener_lista_partidos()
    return jsonify(partidos)

# --------------------- CREAR PARTIDO --------------------- #
@partidos_bp.route("/partidos", methods = ['POST'])
def crear_partido():
    data = request.json
    partidos_service.crear_partido(data)
    return {"message": "Partido creado exitosamente"}, 201

# --------------------- LISTA PARTIDO POR ID --------------------- #
@partidos_bp.route("/partidos/<int:id>", methods = ["GET"])
def obtener_partido_por_id(id):
    partido = partidos_service.obtener_partido_por_id(id)
    if partido is None:
        return {"Error": "Partido no encontrado"}, 404
    
    return jsonify(partido), 200

#---------------------- ACTUALIZAR PARTIDOS --------------------- #
@partidos_bp.route("/partidos/<int:id>", methods = ["PUT"])
def remplazar_partido(id):
    data = request.json
    partidos_service.remplazar_partido(id, data)
    return {"message": "Partido actualizado exitosamente"}, 200

#---------------------- ACTUALIZAR PARCIALMENTE PARTIDOS --------------------- #
#Estaba entre actualizar_parcialmente_partido o solo actualizar_partido #
@partidos_bp.route("/partidos/<int:id>", methods = ["PATCH"])
def actualizar_parcialmente_partido(id):
    data = request.json
    partidos_service.actualizar_parcialmente_partido(id, data)
    return {"message": "Partido actualizado exitosamente"}, 200

# --------------------- BORRAR PARTIDO --------------------- #
@partidos_bp.route("/partidos/<int:id>", methods=["DELETE"])
def delete_partido(id):
    if id <= 0:
            return {"error": "ID invalido"}, 400
    resultado = partidos_service.delete_partido(id)

    if resultado is False:
            return {"error": "Partido no encontrado"}, 404

    if resultado is None:
            return {"error": "Error al eliminar el partido"}, 500
    
    return {"message": "Partido eliminado exitosamente"}, 200

#--------------------- RESULTADO PARTIDO POR ID --------------------- #
@partidos_bp.route("/partidos/<int:id>/resultado", methods=["PUT"])
def actualizar_resultado_partido(id):
    data = request.json
    partidos_service.actualizar_resultado_partido(id, data)
    return {"message": "Resultado del partido actualizado exitosamente"}, 200