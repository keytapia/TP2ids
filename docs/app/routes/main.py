from flask import Blueprint, jsonify

main_bp = Blueprint("main", __name__)


# --------------------- RUTA DE INICIO --------------------- #
@main_bp.route("/", methods=["GET"])
def inicio():
    return "Hello word"

#PARTIDOS
@main_bp.route("/partidos", methods=["GET"])
def partidos():
    return "Lista de partidos"

@main_bp.route("/partidos", methods=["POST"])
def agregar_partido():
    return "Partido agregado"

@main_bp.route("/partidos/<int:partido_id>", methods=["GET"])
def obtener_partido(partido_id):
    return f"Partido con ID {partido_id}"

@main_bp.route("/partidos/<int:partido_id>", methods=["PUT"])
def actualizar_partido(partido_id):
    return f"Partido con ID {partido_id} actualizado"  

@main_bp.route("/partidos/<int:partido_id>", methods=["DELETE"])
def eliminar_partido(partido_id):
    return f"Partido con ID {partido_id} eliminado" 

@main_bp.route("/partidos/<int:partido_id>", methods=["PATCH"])
def actualizar_partido_parcial(partido_id):
    return f"Partido con ID {partido_id} actualizado parcialmente"    

#RESULTADOS
@main_bp.route("/partidos/<int:partido_id>/resultados", methods=["PUT"])
def actualizar_resultados(partido_id):
    return f"Resultados del partido con ID {partido_id} actualizados"

#PREDICCIONES
@main_bp.route("/predicciones", methods=["POST"])
def agregar_prediccion():
    return "Prediccion agregada"   

#USUARIOS
@main_bp.route("/usuarios", methods=["GET"])
def usuarios():
    return "Lista de usuarios"

@main_bp.route("/usuarios", methods=["POST"])
def agregar_usuario():
    return "Usuario agregado"

@main_bp.route("/usuarios/<int:usuario_id>", methods=["GET"])
def obtener_usuario(usuario_id):
    return f"Usuario con ID {usuario_id}"  

@main_bp.route("/usuarios/<int:usuario_id>", methods=["PUT"])
def actualizar_usuario(usuario_id):
    return f"Usuario con ID {usuario_id} actualizado"   

@main_bp.route("/usuarios/<int:usuario_id>", methods=["DELETE"])
def eliminar_usuario(usuario_id):
    return f"Usuario con ID {usuario_id} eliminado"

#RANKING
@main_bp.route("/ranking", methods=["GET"])
def ranking():
    return "Ranking de usuarios"  