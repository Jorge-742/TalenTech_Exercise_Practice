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
