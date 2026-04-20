#!/bin/bash

DB_NAME="prode_db"

echo "Creando la base de datos para el TP2 de IDS!"
echo -e "\nPrimero verificamos si la base de datos '$DB_NAME' ya existe..."
echo -e "\t(ingresá tu contraseña del usuario root de tu MySQL)"

if mysql -u root -p -e "USE $DB_NAME" 2>/dev/null; then
	echo -e "\nLa base de datos ya existe. No se crea nuevamente."
else
	echo "La base de datos '$DB_NAME' no existe"
	echo "Creando base de datos '$DB_NAME'..."
	echo -e "\t(ingresá nuevamente tu contraseña del usuario root de tu MySQL)"

	if mysql -u root -p < docs/database.sql; then
		echo -e "\nBase de datos creada correctamente!"
	else
		echo -e "\nError al crear la base de datos."
	fi
fi
