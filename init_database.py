# /init_database.py
import sys
import os
from datetime import datetime

# --- Configuración para importar desde 'sistema' ---
# Añade el directorio raíz al path de Python
# Esto asegura que podemos hacer 'from sistema import ...'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)
# --------------------------------------------------

try:
    from sistema import create_app, db
    # Importa TODAS tus clases de Modelo
    from sistema.models.marca import Marca
    from sistema.models.modelo import Modelo
    from sistema.models.vehiculo import Vehiculo
    from sistema.models.cliente import Cliente
    from sistema.models.empleado import Empleado
    from sistema.models.alquiler import Alquiler
    from sistema.models.mantenimiento import Mantenimiento
    from sistema.models.multa import Multa
except ImportError as e:
    print(f"Error: No se pudieron importar los módulos. Asegúrate de que __init__.py esté bien configurado.")
    print(f"Detalle: {e}")
    sys.exit(1)

print("Iniciando la creación de la base de datos...")

# 1. Crea la app usando la factory
app = create_app()

# 2. Trabaja dentro del "contexto" de la aplicación
#    Esto es necesario para que SQLAlchemy sepa a qué app
#    y a qué base de datos está conectado.
with app.app_context():
    print("Eliminando tablas antiguas (si existen)...")
    # 3. Elimina todas las tablas existentes (para un reinicio limpio)
    db.drop_all()
    print("Tablas antiguas eliminadas.")

    # 4. Crea todas las tablas nuevas basadas en tus clases Modelo
    db.create_all()
    print("Tablas nuevas creadas exitosamente.")

    # 5. POBLAR LA BASE DE DATOS (Seeding)
    #    Ahora creamos objetos de Python y SQLAlchemy los traduce a SQL.
    print("Poblando la base de datos con datos de ejemplo...")

    try:
        # --- Marcas ---
        m_toyota = Marca(nombre='Toyota')
        m_ford = Marca(nombre='Ford')
        m_chevrolet = Marca(nombre='Chevrolet')

        db.session.add_all([m_toyota, m_ford, m_chevrolet])
        # Commit para que las marcas obtengan sus IDs antes de usarlas
        db.session.commit()
        print("Marcas creadas.")

        # --- Modelos ---
        mo_corolla = Modelo(marca=m_toyota, descripcion='Corolla')
        mo_hilux = Modelo(marca=m_toyota, descripcion='Hilux')
        mo_fiesta = Modelo(marca=m_ford, descripcion='Fiesta')
        mo_onix = Modelo(marca=m_chevrolet, descripcion='Onix')

        db.session.add_all([mo_corolla, mo_hilux, mo_fiesta, mo_onix])
        db.session.commit()  # Commit para los modelos
        print("Modelos creados.")

        # --- Vehículos ---
        v1 = Vehiculo(modelo=mo_corolla, anio=2022, tipo='Sedan', patente='AA123BB', costo_diario=15000)
        v2 = Vehiculo(modelo=mo_hilux, anio=2023, tipo='Camioneta', patente='AD456CC', costo_diario=25000)
        v3 = Vehiculo(modelo=mo_fiesta, anio=2021, tipo='Hatchback', patente='AE789DD', costo_diario=12000)
        v4 = Vehiculo(modelo=mo_onix, anio=2022, tipo='Hatchback', patente='AF111EE', estado='Alquilado',
                      costo_diario=13000)

        db.session.add_all([v1, v2, v3, v4])
        print("Vehículos creados.")

        # --- Clientes ---
        c1 = Cliente(nombre='Juan', apellido='Perez', dni='30123456', email='juan@email.com')
        c2 = Cliente(nombre='Maria', apellido='Garcia', dni='32987654', email='maria@email.com')

        db.session.add_all([c1, c2])
        print("Clientes creados.")

        # --- Empleados ---
        e1 = Empleado(nombre='Admin', apellido='Sistema', dni='12345678', rol='Administrador')

        db.session.add(e1)
        print("Empleados creados.")

        # --- Alquiler de Ejemplo ---
        # (Para el vehículo que ya está 'Alquilado')
        a1 = Alquiler(
            cliente=c2,
            empleado=e1,
            vehiculo=v4,
            fecha_inicio=datetime(2025, 11, 1),  # Fecha de ejemplo
            estado='Activo'
        )
        db.session.add(a1)
        print("Alquiler de ejemplo creado.")

        # Guardar todos los cambios
        db.session.commit()

        print("¡Base de datos poblada exitosamente!")

    except Exception as e:
        db.session.rollback()  # Revertir cambios si hay un error
        print(f"Error al poblar la base de datos: {e}")

print("Proceso de inicialización completado.")

#El ORM hace esto por nosotros. Lee nuestras clases de Python (como class Marca(db.Model) o
# class Vehiculo(db.Model)) y genera el SQL CREATE TABLE automáticamente.


#La función db.create_all() en nuestro nuevo init_database.py es la que le dice a SQLAlchemy: "
# Mira todas las clases que heredan de db.Model y crea las tablas por mí".