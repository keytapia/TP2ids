from app.db import db
from app.models.partido import partido
import re
from datetime import datetime


# --------------------- CREAR PARTIDO --------------------- #
def crear_partido(dato):
    local = dato.get('equipo_local')
    visitante = dato.get('equipo_visitante')
    fecha = dato.get('fecha')
    fase = dato.get('fase')
    goles_local = dato.get('goles_local')
    goles_visitante = dato.get('goles_visitante')


    if not dato.get('equipo_local'):
        return [{
            'code': 400,
            'message': "Faltan campos obligatorios",
            'level': 'error',
            'description': 'El campo "equipo_local" no fue completado y es obligatorio'

        }]

    if not dato.get('equipo_visitante'):
        return [{
            'code': 400,
            'message': "Faltan campos obligatorios",
            'level': 'error',
            'description': 'El campo "equipo_visitante" no fue completado y es obligatorio'

        }]

    if not dato.get('fecha'):
        return [{
            'code': 400,
            'message': "Faltan campos obligatorios",
            'level': 'error',
            'description': 'El campo "fecha" no fue completado y es obligatorio'

        }]

    if not dato.get('fase'):
        return [{
            'code': 400,
            'message': "Faltan campos obligatorios",
            'level': 'error',
            'description': 'El campo "fase" no fue completado y es obligatorio'

        }]


    if local == visitante:
        return [{
            'code': 400,
            'message': "Equipos invalidos",
            'level': 'error',
            'description': 'no se pueden enfrentar los mismos equipos'
        }]

    def validacion_fecha(fecha):
        try:
            datetime.strptime(str(fecha), '%Y-%m-%d %H:%M:%S')
            return True
        except ValueError:
            return False
    if not validacion_fecha(fecha):
        return [{
            'code': 400,
            'message': "Fecha invalida",
            'level': 'error',
            'description': 'Debe ser una fecha valida y tener el formato YYYY-MM-DD'
        }]

    def partido_existente(partido):
        partido_posible =partido_existente = (partido.query.filter_by(local = dato.get('local'),visitante = dato.get('visitante'),fase = dato.get('fase')).first())
        return partido_posible

    if partido_existente(partido):
        return [{
            'code': 409,
            'message': "partido existente",
            'level': 'error',
            'description': 'este partido ya se encuentra registrado en esta fase'
        }]
    nuevo_partido = db.crear(local, visitante, fecha, fase, goles_local, goles_visitante)
    return nuevo_partido, 201


# --------------------- ELIMINAR PARTIDO --------------------- #
def eliminar_partido(id):
    partido_encontrado=partido.query.get(id)
    if not partido_encontrado:
        return 0
    
    db.session.delete(partido_encontrado)
    db.session.commit()

    return 1


# --------------------- OBTENER PARTIDO POR ID --------------------- #
def obtener_partido_por_id(id_buscado):
    return partido.query.get(id_buscado)