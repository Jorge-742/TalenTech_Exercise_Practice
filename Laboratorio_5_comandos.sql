--- Ejercicio de práctica 1.
--- Crea la base de datos.
CREATE DATABASE empresa;
--- Llama o trae la base de datos.
USE empresa;
----------------------------------------------------------------
--- Crea la tabla llamada empleados con sus respectivos campos.
CREATE TABLE empleados (
	id_empleado INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(225) NOT NULL,
    cargo VARCHAR (50) NOT NULL,
    salario DECIMAL);

--- Inserta datos en los campos de la tabla empleados.
INSERT INTO empleados (nombre, cargo, salario)
	VALUES
    	('Juan Pérez', 'Gerente', 7500000),
        ('Ana Gómez', 'Desarrollador', 6000000),
        ('Luis Castro', 'Proyectos', 10000000);
----------------------------------------------------------------
--- Crea la tabla llamada cargos con sus respectivos campos.
CREATE TABLE cargos (
	id_cargo INT PRIMARY KEY AUTO_INCREMENT,
	nombre_cargo VARCHAR(50) NOT NULL,
    descripcion VARCHAR(1000),
	salario DECIMAL);
--- Inserta datos en los campos 'nombre_cargo' y 'salario' de la tabla cargos.
INSERT INTO cargos (nombre_cargo, salario)
	VALUES
    	('Gerente', 500000),
        ('Asistente', 250000),
        ('Desarrollador', 400000);
-----------------------------------------------------------------

--- Consultas y actualizaciones de la base de datos empresa.

--- Selecciona todos los campos de la tabla cargos.
SELECT * 
FROM cargos;

--- Selecciona a los empleados que ganan más de 7000000.
SELECT *
FROM empleados
WHERE salario > 7000000;

--- Actualiza el salario de Ana Gómez de 6000000 a 6500000.
UPDATE empleados
SET salario = 6500000
WHERE nombre = 'Ana Gómez';

--- Elimina el registro del empleado Luis Castro
DELETE 
FROM empleados
WHERE nombre = 'Luis Castro';

--- Selecciona los registros de la tabla empleados en el cual el empleado tenga como cargo desarrollador.
SELECT * 
FROM empleados
WHERE cargo = 'Desarrollador';

--- Agregación de un nuevo empleado
INSERT INTO empleados(nombre, cargo, salario)
	VALUES
		('Marta López', 'Asistente', 3000000)
----------------------------------------------------------------


--- Parte 2. Modificación de la base de datos biblioteca
USE biblioteca;

--- Actualización de la disponibilidad de un libro
UPDATE libros
SET disponible = FALSE
WHERE id_libro = 1;

--- Actualización de la fecha de devolución de un préstamo
UPDATE prestamos
SET fecha_devolucion = '2024-08-30'
WHERE id_prestamo = 1;

--- Eliminación de un libro de la base de datos
DELETE FROM libros
WHERE id_libro = 3;

--- Selección de todos los libros 
SELECT *
FROM libros;

--- Selección de todos los autores
SELECT *
FROM autores;

--- Selección del libro de Gabriel García Marquéz
SELECT *
FROM libros
WHERE id_autor = 1;

--- Vista de libro devueltos en el mes 8 del año 2024
--- Solución 1
SELECT *
FROM prestamos
WHERE fecha_devolucion BETWEEN '2024-08-01' AND '2024-08-30';
--- solución 2
SELECT * 
FROM Prestamos
WHERE MONTH(Fecha_Devolucion) = 8 AND YEAR(Fecha_Devolucion) = 2024;
