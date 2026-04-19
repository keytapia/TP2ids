from app.db import db
from app.db import get_connection
import re
from datetime import datetime

# --------------------- PREDICCION --------------------- #
def crear_prediccion(id_partido, data):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO predicciones (usuario_id, id_partido, equipo_local, equipo_visitante, resultado_predicho) VALUES (%s, %s, %s, %s, %s)""", (data.get('usuario_id'), id_partido, data.get('equipo_local'), data.get('equipo_visitante'), data.get('resultado_predicho')))
            connection.commit()
            return True
    except Exception as e:
        print("Error al crear la prediccion:", e)
        return None
    finally:
        connection.close()