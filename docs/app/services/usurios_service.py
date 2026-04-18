
from app.db import db
from app.models.usuario import usuario

#DELETE

def eliminar_usuario(id):
    usuario_encontrado=usuario.query.get(id)
    if not usuario_encontrado:
        return 0
    
    db.session.delete(usuario_encontrado)
    db.session.commit()

    return 1
