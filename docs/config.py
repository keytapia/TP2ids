# configuracion general, conexion MySQL y settings
class Config:
    # Configuración de la base de datos MySQL
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/myapp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False