from app.db import get_connection
import re

def obtener_ranking():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT u.id, u.nombre, u.email, COUNT(p.id) AS publicaciones_count
                FROM usuarios u
                LEFT JOIN publicaciones p ON u.id = p.usuario_id
                GROUP BY u.id
                ORDER BY publicaciones_count DESC
            """)
            ranking = cursor.fetchall()
            return ranking
    finally:
        connection.close()