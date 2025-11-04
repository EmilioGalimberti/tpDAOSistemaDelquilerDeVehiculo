-- Elimina las tablas si ya existen (para poder reiniciar fácilmente)
DROP TABLE IF EXISTS alquiler;
DROP TABLE IF EXISTS mantenimiento;
DROP TABLE IF EXISTS vehiculos;
DROP TABLE IF EXISTS modelos;
DROP TABLE IF EXISTS marcas;
DROP TABLE IF EXISTS clientes;
DROP TABLE IF EXISTS empleados;

-- Tabla de Marcas de Vehículos
CREATE TABLE marcas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL UNIQUE
);

-- Tabla de Modelos de Vehículos
CREATE TABLE modelos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_marca INTEGER NOT NULL,
    descripcion TEXT NOT NULL,
    FOREIGN KEY (id_marca) REFERENCES marcas (id)
);

-- Tabla de Vehículos
CREATE TABLE vehiculos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_modelo INTEGER NOT NULL,
    anio INTEGER NOT NULL,
    tipo TEXT NOT NULL, -- (Ej. 'Sedan', 'SUV', 'Camioneta')
    patente TEXT NOT NULL UNIQUE,
    -- El estado es crucial para tu lógica de negocio
    estado TEXT NOT NULL DEFAULT 'Disponible', -- (Disponible, Alquilado, En Mantenimiento)
    costo_diario REAL NOT NULL,
    FOREIGN KEY (id_modelo) REFERENCES modelos (id)
);

-- Tabla de Clientes
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    dni TEXT NOT NULL UNIQUE,
    direccion TEXT,
    telefono TEXT,
    email TEXT UNIQUE
    -- Según el ABM de Clientes[cite: 18], aquí faltarían datos de licencia
);

-- Tabla de Empleados
CREATE TABLE empleados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    dni TEXT NOT NULL UNIQUE,
    direccion TEXT,
    rol TEXT NOT NULL,
    telefono TEXT,
    email TEXT UNIQUE
);

-- Tabla de Alquiler (La transacción principal) [cite: 20]
CREATE TABLE alquiler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER NOT NULL,
    id_empleado INTEGER NOT NULL,
    id_vehiculo INTEGER NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE, -- Se actualiza en la devolución [cite: 22]
    costo_total REAL, -- Se calcula al finalizar [cite: 23]
    estado TEXT NOT NULL DEFAULT 'Activo', -- (Activo, Finalizado)
    FOREIGN KEY (id_cliente) REFERENCES clientes (id),
    FOREIGN KEY (id_empleado) REFERENCES empleados (id),
    FOREIGN KEY (id_vehiculo) REFERENCES vehiculos (id)
);

-- Tabla de Mantenimiento (Extensión Opcional)
CREATE TABLE mantenimiento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_vehiculo INTEGER NOT NULL,
    fecha DATE NOT NULL,
    descripcion TEXT,
    costo REAL,
    tipo TEXT, -- (Preventivo, Correctivo)
    FOREIGN KEY (id_vehiculo) REFERENCES vehiculos (id)
);

-- Inserta algunos datos de ejemplo (opcional pero recomendado)
INSERT INTO marcas (nombre) VALUES ('Toyota'), ('Ford'), ('Chevrolet');
INSERT INTO modelos (id_marca, descripcion) VALUES (1, 'Corolla'), (1, 'Hilux'), (2, 'Fiesta'), (3, 'Onix');
INSERT INTO vehiculos (id_modelo, anio, tipo, patente, costo_diario)
VALUES
    (1, 2022, 'Sedan', 'AA123BB', 15000),
    (2, 2023, 'Camioneta', 'AD456CC', 25000),
    (3, 2021, 'Hatchback', 'AE789DD', 12000);

INSERT INTO clientes (nombre, apellido, dni, email)
VALUES ('Juan', 'Perez', '30123456', 'juan@email.com');

INSERT INTO empleados (nombre, apellido, dni, rol)
VALUES ('Admin', 'Sistema', '12345678', 'Administrador');