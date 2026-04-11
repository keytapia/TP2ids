#esto es solo de prueba para ver con python run.py si todo funciona y si Flask corre
from flask import Blueprint

main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=["GET"])
def inicio():
    return "Hello word"
