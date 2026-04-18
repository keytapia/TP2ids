from app.db import db
from app.models.usuario import usuario
#import re (no se si hay que ponerlo para que funcione)
import re


def crear_usuario(dato):

    if not dato.get('nombre'):
        return [{
            'code': 400,
            'message': 'Faltan datos obligatorios',
            'level': 'error',
            'description': 'El campo "nombre" no fue completado y es obligatorio'
        }]
    if not dato.get('email'):
        return [{
            'code': 400,
            'message': 'Faltan datos obligatorios',
            'level': 'error',
            'description': 'El campo "email" no fue completado y es obligatorio'
        }]
    if usuario.query.filter_by(email=dato.get('email')).first():
        return [{
            'code': 409,
            'message': 'Este email ya esta siendo utilizado',
            'level': 'error',
            'description': 'Este email ya esta siendo utilizado'
        }]
    if not re.match(r"[^@]+@[^@]+\.[^@]+", dato.get('email')):
        return [{
            'code': 400,
            'message': 'Email invalido',
            'level': 'error',
            'description': 'el formato de email es invalido'
        }]

    nombre = dato.get('nombre')
    email = dato.get('email')
    nuevo_usuario = db.crear(nombre, email)
    return nuevo_usuario, 201
