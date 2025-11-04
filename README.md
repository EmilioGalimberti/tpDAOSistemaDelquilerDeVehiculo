# 🚗 Sistema de Alquiler de Vehículos - Grupo 33

Este proyecto es el trabajo práctico integrador para la materia "Desarrollo de Aplicaciones con Objetos". El objetivo es construir una aplicación web de gestión integral para una empresa de alquiler de vehículos.

## 🎯 Objetivos del Sistema

### Objetivo General
[cite_start]Desarrollar una aplicación de gestión integral que permita administrar la flota, los clientes y el proceso de alquiler de forma eficiente[cite: 7].

### Objetivos Específicos
* [cite_start]Implementar las operaciones **CRUD** (Altas, Bajas, Modificaciones y Consultas) para Vehículos, Clientes y Empleados[cite: 9].
* [cite_start]Gestionar la transacción principal de **"Alquiler"**, validando la disponibilidad de los vehículos[cite: 10, 21].
* [cite_start]Proveer **reportes** y estadísticas sobre la operación (ej. vehículos más alquilados, facturación)[cite: 11].

---

## 🛠️ Stack Tecnológico y Requerimientos

Este proyecto utiliza un stack simple pero potente para aplicar los conceptos de POO y desarrollo web:

* **Python:** Como lenguaje principal de programación.
* **Flask:** Un "micro-framework" web. Lo usamos para construir nuestros **Controladores** (recibir peticiones HTTP de las URLs) y renderizar las **Vistas** (plantillas HTML).
* **SQLite:** Un motor de base de datos relacional ligero basado en archivos. Lo usamos como nuestro **Modelo** para persistir los datos de la aplicación (vehículos, clientes, etc.).

### Archivo de Requerimientos
Para instalar las dependencias, asegúrate de que tu archivo `requirements.txt` contenga:

```txt
Flask
```

---

## 🚀 Cómo Empezar

Sigue estos pasos para levantar el entorno de desarrollo local:

1.  **Crear un Entorno Virtual** (Recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

2.  **Instalar Dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Inicializar la Base de Datos**:
    (Solo necesitas hacerlo la primera vez, o si borras `alquileres.db`)
    ```bash
    python init_database.py
    ```

4.  **Ejecutar el Servidor**:
    ```bash
    python run.py
    ```

5.  **Abrir la Aplicación**:
    Visita `http://127.0.0.1:5000/` en tu navegador.

---

## 📁 Estructura del Proyecto

El proyecto está organizado siguiendo el patrón arquitectónico **MVC (Modelo-Vista-Controlador)** para mantener una clara separación de responsabilidades.

```
/sistema_alquileres_project/
|
|-- /sistema/                <-- Paquete principal de la aplicación Flask
|   |-- __init__.py          # "Fábrica" de la app: Crea la app y registra los Controladores (Blueprints)
|   |-- database.py          # Módulo para manejar la conexión a la BD (get_db_connection)
|   |
|   |-- /controllers/        <-- (C) CONTROLADORES (Lógica de Rutas)
|   |   |-- __init__.py
|   |   |-- main_controller.py   # Blueprint para rutas principales (/, /index)
|   |   |-- (futuro) vehiculo_controller.py  # Blueprint para /vehiculos, /vehiculos/nuevo, etc.
|   |
|   |-- /models/             <-- (M) MODELOS (Lógica de Negocio y Datos)
|   |   |-- __init__.py
|   |   |-- (futuro) vehiculo.py # Contendrá la clase Vehiculo, EstadoVehiculo, etc.
|   |
|   |-- /templates/          <-- (V) VISTAS (Plantillas HTML)
|   |   |-- index.html
|   |
|   |-- /static/             <-- Archivos estáticos (CSS, JS, imágenes)
|
|-- run.py                   # Script de arranque (Inicia el servidor web)
|-- init_database.py         # Script para crear la BD desde cero usando schema.sql
|-- schema.sql               # Definición SQL de todas las tablas
|-- alquileres.db            # El archivo de la base de datos SQLite (creado por init_database.py)
|-- requirements.txt         # Lista de dependencias de Python
|-- README.md                # Esta documentación
```

---

## 🎨 Patrones de Diseño Aplicados (ESTO TODAVIA REVISAR)

[cite_start]Además de MVC, el proyecto busca implementar patrones de diseño de POO para resolver problemas comunes[cite: 13]:

1.  **Patrón State (Estado)**:
    * [cite_start]**Problema:** Un `Vehiculo` tiene estados que cambian su comportamiento (ej. "Disponible", "Alquilado", "En Mantenimiento")[cite: 21]. No queremos `if/else` gigantes en la clase `Vehiculo`.
    * **Solución:** Crearemos una interfaz `EstadoVehiculo` y clases concretas (`EstadoDisponible`, `EstadoAlquilado`). La clase `Vehiculo` *delegará* el comportamiento (como `alquilar()` o `devolver()`) a su objeto de estado actual.

2.  **Patrón Factory (Fábrica)**:
    * [cite_start]**Problema:** El sistema necesita generar diferentes tipos de reportes (ej. "Alquileres por Cliente", "Vehículos Más Alquilados")[cite: 11, 26, 28].
    * **Solución:** Crearemos una `ReportFactory` que reciba un tipo de reporte y devuelva el objeto de reporte correcto, listo para ser procesado.

3.  **Patrón Strategy (Estrategia)**:
    * [cite_start]**Problema:** El cálculo del costo de un alquiler puede cambiar[cite: 23]. Podríamos tener una tarifa diaria simple, una tarifa con descuento por semana, o una tarifa especial de fin de semana.
    * **Solución:** Crearemos una interfaz `EstrategiaDeCalculo` y clases concretas (`CalculoTarifaDiaria`, `CalculoTarifaSemanal`). La clase `Alquiler` usará una de estas estrategias para determinar el `costo_total` sin que la clase `Alquiler` sepa los detalles del cálculo.