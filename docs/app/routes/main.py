from flask import Blueprint, jsonify

main_bp = Blueprint("main", __name__)


# --------------------- RUTA DE INICIO --------------------- #
@main_bp.route("/", methods=["GET"])
def inicio():
    return jsonify({
        "message": "La API esta funcionando joya"
    }), 200