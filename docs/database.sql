CREATE DATABASE IF NOT EXISTS prode_db;
USE prode_db;

CREATE TABLE usuarios(
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE partidos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  equipo_local VARCHAR(100) NOT NULL,
  equipo_visitante VARCHAR(100) NOT NULL,
  fecha DATETIME NOT NULL,
  fase VARCHAR(50) NOT NULL,
  goles_local INT,
  goles_visitantes INT
);

CREATE TABLE predicciones (
  id INT AUTO_INCREMENT PRIMARY KEY,
  usuario_id INT NOT NULL,
  partido_id INT NOT NULL,
  pred_local INT NOT NULL,
  pred_visitante INT NOT NULL,
  
  CONSTRAINT unique_prediccion UNIQUE(usuario_id, partido_id),
  
  CONSTRAINT fk_usuario
    FOREIGN KEY (usuario_id)
    REFERENCES usuarios(id)
    ON DELETE CASCADE,
  
  CONSTRAINT fk_partido
    FOREIGN KEY (partido_id)
    REFERENCES partidos(id)
    ON DELETE CASCADE
  );
