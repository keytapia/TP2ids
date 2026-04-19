from flask import Flask
from app.routes.main import main_bp
from app.routes.usuarios import usuarios_bp
from app.routes.partidos import partidos_bp
from app.routes.predicciones import predicciones_bp
from app.routes.ranking import ranking_bp

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(main_bp)
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(partidos_bp)
    app.register_blueprint(ranking_bp)
    app.register_blueprint(predicciones_bp)
    
    return app
