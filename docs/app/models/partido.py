from app.db import db

class partido(db.Model):

    __tablename__ = 'partidos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    equipo_local = db.Column(db.String(100), nullable=False)
    equipo_visitante = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    fase = db.Column(db.String(50), nullable=False)
    goles_local = db.Column(db.int, nullable=True)
    goles_visitante = db.Column(db.int, nullable=True)