from app.db import db
from app.models.usuario import usuario
from app.models.usuario import usuario
import re


#--------------------- OBTENER LISTA USUARIOS --------------------- #
def obtener_lista_usuarios():
    try:
        usuarios = usuario.query.all()
        return [u.to_dict() for u in usuarios]
    except Exception as e:
        print("Error al obtener la lista de usuarios:", e)
        return None