from flask import Flask
from app.db import db
from app.routes.main import main_bp #conecta con docs/app/routes/main.py

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    
    app.register_blueprint(main_bp)
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(partidos_bp)
    
    return app
