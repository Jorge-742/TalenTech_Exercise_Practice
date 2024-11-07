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

--- Crea la tabla 'Categorias' y demás elementos.
CREATE TABLE Categorias (
	id_categoria INT PRIMARY KEY AUTO_INCREMENT,
	nombre_categoria VARCHAR(100) NOT NULL);

--- Inserta datos en los campos de la tabla 'Categorias'
INSERT INTO categorias (nombre_categoria)
	VALUES
    		('Novela'),
		('Ciencia Ficción'),
		('Fantasía'),
		('Ensayo');
-------------------------------------------------------------------------------------------
--- Crea la tabla 'Libros' con sus campos, tipos de datos, llave primaria y llave foranéa.
CREATE TABLE Libros (
	id_libro INT PRIMARY KEY AUTO_INCREMENT,
	titulo VARCHAR(225) NOT NULL,
    	id_autor INT,
    	id_categoria INT,
	FOREIGN KEY (id_autor) REFERENCES Autores (id_autor),
	FOREIGN KEY (id_categoria) REFERENCES Categorias (id_categoria),
	año_publicacion INT,
	disponible BOOLEAN DEFAULT TRUE);

--- Inserta datos en los campos de la tabla 'Libros'.
INSERT INTO libros (titulo, id_autor, id_categoria, año_publicacion)
	VALUES
		('Cien Años de Soledad', 1, 1, 1967),
		('Harry Potter y la Piedra Filosofal', 2, 3, 1997),
		('1984', 3, 2, 1949);
--------------------------------------------------------------------------------------------
--- Crea la tabla 'Usuarios' y demás elementos.
CREATE TABLE Usuarios (
    	id_usuario INT PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(100) NOT NULL,
	direccion VARCHAR(225) NOT NULL,
	telefono INT(20));

--- Inserta datos en los campos de la tabla 'Usuarios'.
INSERT INTO usuarios (nombre, direccion, telefono)
	VALUES
    	('Carlos Martínez', 'Calle Luna, 123', '123456789'),
        ('Lucía Fernández', 'Avenida Sol, 456', ' 987654321');
--------------------------------------------------------------------------------------------
--- Crea la tabla 'Prestamos' y demás elementos.
CREATE TABLE Prestamos (
	id_prestamo INT PRIMARY KEY AUTO_INCREMENT,
	id_usuario INT,
	id_libro INT,
	fecha_prestamo DATE,
	fecha_devolucion DATE,
	FOREIGN KEY (id_usuario) REFERENCES Usuarios (id_usuario),
	FOREIGN KEY (id_libro) REFERENCES Libros (id_libro));

--- Inserta datos en los campos de la tabla 'Prestamos'.
INSERT INTO prestamos (id_usuario, id_libro, fecha_prestamo, fecha_devolucion)
	VALUES
    	(1, 1, '2024-08-01', '2024-08-15'),
        (2, 2, ' 2024-08-02', '2024-08-16');
--------------------------------------------------------------------------------------------
--- Crea la tabla relacionada 'Prestamos_usuarios', con sus campos, llave primaria y llaves foranéas. Ello le permite relacionar la información de diferentes tablas.
CREATE TABLE Prestamos_usuarios (
	id_prestamo_usuario INT PRIMARY kEY AUTO_INCREMENT,
	id_prestamo INT NOT NULL,
	Id_usuario INT NOT NULL,
	FOREIGN KEY (id_prestamo) REFERENCES prestamos (id_prestamo),
	FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario)
);
