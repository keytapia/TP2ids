from flask import Blueprint, jsonify, request

from app.services import ranking_service
from app.services.ranking_service import obtener_ranking

ranking_bp = Blueprint("ranking", __name__)
@ranking_bp.route("/ranking", methods=["GET"])
def ranking():
    ranking = ranking_service.obtener_ranking()
    if not ranking:
        return {"Error": "No se encontraron usuarios"}, 404
    return jsonify(ranking), 200