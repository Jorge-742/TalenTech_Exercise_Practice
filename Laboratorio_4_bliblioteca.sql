--- Crea la base de datos 'biblioteca'.
CREATE DATABASE biblioteca;

--- Llama la base de datos.
USE biblioteca;

---------------------------------------------------------------------------------------------
 --- crea la tabla de 'Autores' con sus respectivos campos, tipos de datos y clave primaria.
CREATE TABLE Autores (
	id_autor INT PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(100) NOT NULL,
	nacionalidad VARCHAR(100),
	fecha_nacimiento DATE);

--- Inserta datos en los campos de la tabla 'Autores'.
INSERT INTO autores (nombre, nacionalidad, fecha_nacimiento)
	VALUES
    	('Gabriel Garcia Márquez', 'Colombiano', '1927-03-06'),
        ('J.K. Rowling', 'Británica', '1965-07-31'),
        ('George Orwell', 'Británica', '1903-06-25');

-------------------------------------------------------------------------------------------
