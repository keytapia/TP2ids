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


## Cómo ejecutar la API

Abrí tu terminal en la carpeta del proyecto (y con el entorno virtual activado), y ejecutá el siguiente comando:

`flask run`

Vas a ver un mensaje en la terminal indicando que el servidor está corriendo localmente en tu computadora en el puerto 5000 (usualmente en `http://127.0.0.1:5000` o `http://localhost:5000`).

Dejá esta terminal abierta.


## Endpoints Disponibles

La API expone los siguientes recursos bajo la ruta `/`:

| **Verbo HTTP** | **Endpoint**     | **Descripción**              |
|----------------|------------------|------------------------------|
| GET            | `/0`             | Acá ponemos que hacen        |
| POST           | `/1`             | Acá ponemos que hacen        |
| PUT            | `/2`             | Acá ponemos que hacen        |
| DELETE         | `/3`             | Acá ponemos que hacen        |
