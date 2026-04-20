# TP2 de IDS - Proyecto Backend

Este proyecto consiste en el desarrollo de una API Backend para la gestión de un sistema de predicciones deportivas (ProDe) basado en la Copa Mundial de la FIFA 2026.

La aplicación permite constuir y administrar un fixture de partidos, registrar encuentros, actualizar los resultados una vez finalizados los partidos y consultar partidos mediante distintos criterios.

Está diseñada en base a un contrato Swagger y desarrollada como una API REST en Python con Flask y base de datos SQL.


## Alumnos

| **Padrón** | **Apellido**     | **Nombre**           |
|------------|------------------|----------------------|
| 115658     | KERSUL           | Celeste Briza        |
| 114292     | LICHINIZER       | Valeria Dana         |
| 115563     | MARTIN           | Miguel               |
| 112615     | NAYA NICOLAS     | Camila Rocío         |
| 115403     | NOVILLO          | Marilyn Jessenia     |
| 111274     | ROMERO           | Gonzalo Nahuel       |
| 106820     | SCALISE          | Federico Nahuel      |
| 112048     | SILVA            | Franco Gabriel       |
| 115130     | TAPIA            | Keyla                |


## Requisitos Previos

Necesitás tener instalado el intérprete de [Python](https://www.python.org/downloads) en tu computadora. Este proyecto fue probado con Python 3.12.3.

Además necesitás tener instalado el motor de [MySQL](https://dev.mysql.com/downloads/mysql/)
- En Linux: Podes ejecutar desde la terminal los siguientes comandos
`sudo apt update`
`sudo apt install mysql-server`


## Instalación y Configuración

Seguí estos pasos para ejecutar la API en tu entorno local:

1.  **Cloná este repositorio** (o descargá los archivos en una carpeta):  
    *Clonamos el repositorio:*  
    `git clone git@github.com:keytapia/TP2ids.git`  
    *Accedemos a la carpeta:*  
    `cd TP2ids`  
2.  **Creá un entorno virtual**:  
    *Creamos el entorno virtual venv en una carpeta oculta llamada "venv":*  
    `python3 -m venv .venv`  
    *Activamos el entorno virtual:*  
    - En Windows: `.venv\Scripts\activate`  
    - En macOS/Linux: `source .venv/bin/activate`  
3.  **Instalá las dependencias**:  
    *Con este comando instalamos lo que se detalla dentro del archivo requirements.txt*  
    `pip install -r requirements.txt`
4.  **Creá la base de datos 'prode_db'** (Se utilizará para el proyecto)
    *Tenes que ejecutar el script 'crear_bd.sh' provisto en el respositorio, el cual ya ejecuta los comandos necesarios para poder crear la base de datos.*
    *Primero le damos permiso de ejecución:*
    `chmod +x crear_bd.sh`
    *Luego lo ejecutamos*
    `./crear_bd.sh`
    *Nota: Te pedirá la contraseña del usuario root de MySQL*


## Cómo ejecutar la API

Abrí tu terminal en la carpeta del proyecto (y con el entorno virtual activado), y ejecutá el siguiente comando:

`python run.py`

Vas a ver un mensaje en la terminal indicando que el servidor está corriendo localmente en tu computadora en el puerto 5000 (usualmente en `http://127.0.0.1:5000` o `http://localhost:5000`).

Dejá esta terminal abierta.


## Endpoints Disponibles

La API expone los siguientes recursos bajo la ruta `/`:

**- Partidos**
| **Verbo HTTP** | **Endpoint**     | **Descripción**              |
|----------------|------------------|------------------------------|
| GET            | `/partidos`             | Listar partidos (sin resultados incluidos)        |
| POST           | `/partidos`             | Crear partido        |
| GET            | `/partidos/{id}`             | Obtener un partido por ID        |
| PUT         | `/partidos/{id}`             | Reemplazar un partido        |
| PATCH            | `/partidos/{id}`             | Actualizar parcialmente un partido        |
| DELETE         | `/partidos/{id}`             | Eliminar un partido        |

**- Resultados**
| **Verbo HTTP** | **Endpoint**     | **Descripción**              |
|----------------|------------------|------------------------------|
| PUT            | `/partidos/{id}/resultado`             | Actualizar resultado        |

**- Predicciones**
| **Verbo HTTP** | **Endpoint**     | **Descripción**              |
|----------------|------------------|------------------------------|
| POST            | `/partidos/{id}/prediccion`             | Registrar una predicción para un partido        |

**- Usuarios**
| **Verbo HTTP** | **Endpoint**     | **Descripción**              |
|----------------|------------------|------------------------------|
| GET            | `/usuarios`             | Listar usuarios        |
| POST           | `/usuarios`             | Crear usuarios        |
| GET            | `/usuarios/{id}`             | Obtener un usuario por ID        |
| PUT         | `/usuarios/{id}`             | Reemplazar un usuario        |
| DELETE         | `/usuarios/{id}`             | Eliminar usuario        |

**- Ranking**
| **Verbo HTTP** | **Endpoint**     | **Descripción**              |
|----------------|------------------|------------------------------|
| GET            | `/ranking`             | Obtener el ranking de usuarios        |

