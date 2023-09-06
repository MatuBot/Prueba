CREATE DATABASE IF NOT EXISTS proyecto_db; 

USE proyecto_db; 

CREATE TABLE Personas (
    DNI INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    fecha_nacimiento DATE,
    GBA BOOLEAN
);

INSERT INTO Personas (DNI, nombre, apellido, fecha_nacimiento, GBA) VALUES
(123456789, 'Juan', 'Pérez', '1990-05-15', true),
(987654321, 'María', 'González', '1985-03-20', false),
(456789123, 'Pedro', 'López', '1998-11-10', true),
(789123456, 'Laura', 'Fernández', '1992-07-25', false),
(321654987, 'Carlos', 'Martínez', '1980-09-05', true),
(556987423, 'Ana', 'Sánchez', '1995-02-18', true),
(678953215, 'Luis', 'Ramírez', '1977-12-30', false),
(712354897, 'Mónica', 'Díaz', '1997-08-08', true),
(832549876, 'Roberto', 'Torres', '1982-04-12', false),
(945698731, 'Elena', 'Vargas', '1989-06-03', true),
(103876221, 'Diego', 'Luna', '1987-10-22', false),
(256406545, 'Natalia', 'Hernández', '1993-03-14', true),
(332156748, 'Gustavo', 'Sosa', '1996-01-29', false),
(445100354, 'Valentina', 'Romero', '1994-09-02', true),
(557851350, 'José', 'Gómez', '1986-07-11', false),
(665420354, 'Camila', 'Paz', '1991-12-05', true),
(704850685, 'Martín', 'Silva', '1983-06-28', false),
(887896506, 'Mariana', 'López', '1990-04-17', true),
(954687620, 'Santiago', 'Rojas', '1984-08-24', false),
(101236905, 'Alejandra', 'García', '1998-10-01', true);