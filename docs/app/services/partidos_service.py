from app.db import db
from app.db import get_connection
import re
from datetime import datetime

#--------------------- OBTENER LISTA PARTIDOS --------------------- #
def obtener_lista_partidos():
   connection = get_connection()

   try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM partidos")
            partidos = cursor.fetchall()
        return partidos
    finally:
        connection.close()

# --------------------- LISTA PARTIDO POR ID --------------------- #
def obtener_partido_por_id(id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM partidos WHERE id = %s", (id,))
            partido = cursor.fetchone()
        return partido
    finally:
        connection.close()

# --------------------- CREAR PARTIDO --------------------- #
def crear_partido(dato):
    conection = get_connection()
    try:
        with conection.cursor() as cursor:
            cursor.execute("""INSERT INTO partidos (equipo_local, equipo_visitante, fecha, fase) VALUES (%s, %s, %s, %s)""", (dato.get('equipo_local'), dato.get('equipo_visitante'), dato.get('fecha'), dato.get('fase')))
            conection.commit()
            return True
    except Exception as e:
        print("Error al crear el partido:", e)
        return None
    finally:
        conection.close()

#--------------------- ACTUALIZAR PARTIDO --------------------- #  
def remplazar_partido(id, data):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE partidos SET equipo_local = %s, equipo_visitante = %s, fecha = %s, fase = %s WHERE id = %s""", (data.get('equipo_local'), data.get('equipo_visitante'), data.get('fecha'), data.get('fase'), id))
            if cursor.rowcount == 0:
                return False
        connection.commit()
        return True
    except Exception as e:
        print("Error al actualizar el partido:", e)
        return None
    finally:
        connection.close()

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