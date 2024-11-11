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
