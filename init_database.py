from sistema import create_app, db
from sistema.models.vehiculo import Vehiculo
from sistema.models.mantenimiento import Mantenimiento
from sistema.models.alquiler import Alquiler
from sistema.models.multa import Multa
from sistema.models.empleado import Empleado
from sistema.models.cliente import Cliente

def init_db():
    """
    Inicializa la base de datos y crea las tablas a partir de los modelos.
    """
    app = create_app()
    with app.app_context():
        print("Creando todas las tablas de la base de datos...")
        db.create_all()
        print("Tablas creadas exitosamente.")

if __name__ == '__main__':
    print("Iniciando la creación de la base de datos...")
    init_db()
    print("Proceso de inicialización completado.")
