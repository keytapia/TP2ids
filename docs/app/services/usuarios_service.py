from app.db import get_connection
import re


#--------------------- OBTENER LISTA USUARIOS --------------------- #
def obtener_lista_usuarios():
   connection = get_connection()
   try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, nombre, email FROM usuarios")
            usuarios = cursor.fetchall()
            return usuarios
   finally:
        connection.close()

#--------------------- BUSCAR USUARIO POR ID --------------------- #
def usuario_por_id(id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, nombre, email FROM usuarios WHERE id = %s", (id,))
            usuario = cursor.fetchone()
            return usuario
    finally:
        connection.close()

#--------------------- CREAR USUARIO --------------------- #
def crear_usuario(data):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO usuarios (nombre, email) VALUES (%s, %s)""", (data.get('nombre'), data.get('email')))
            connection.commit()
            return True
    except Exception as e:
        print("Error al crear el usuario:", e)
        return None
    finally:
        connection.close()

#--------------------- ACTUALIZAR USUARIO --------------------- #
def actualizar_usuario(id, data):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE usuarios SET nombre = %s, email = %s WHERE id = %s""", (data.get('nombre'), data.get('email'), id))
            if cursor.rowcount == 0:
                return False
        connection.commit()
        return True
    except Exception as e:
        print("Error al actualizar el usuario:", e)
        return None
    finally:
        connection.close()  

#--------------------- BORRAR USUARIO --------------------- #
def delete_usuario(id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
            if cursor.rowcount == 0:
                return False
        connection.commit()
        return True
    except Exception as e:
        print("Error al eliminar el usuario:", e)
        return None
    finally:
        connection.close()