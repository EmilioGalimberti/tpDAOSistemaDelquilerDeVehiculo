# /sistema/controllers/vehiculo_controller.py
from flask import Blueprint, render_template
from sistema import db
from sistema.models.vehiculo import Vehiculo
# Importamos Modelo y Marca para poder acceder a la info relacionada
from sistema.models.modelo import Modelo
from sistema.models.marca import Marca

# Creamos el Blueprint para el controlador de Vehículos
vehiculo_bp = Blueprint('vehiculos', __name__)


@vehiculo_bp.route('/')
def listar_vehiculos():
    """
    Ruta para la página que lista todos los vehículos de la flota.
    (Lee la 'R' del CRUD)
    """
    try:
        # 1. Obtenemos todos los vehículos.
        #    Usamos 'options' y 'joinedload' para que SQLAlchemy
        #    traiga los datos del modelo y la marca en la misma consulta.
        #    Esto es una optimización que evita muchas consultas pequeñas.
        vehiculos = Vehiculo.query.options(
            db.joinedload(Vehiculo.modelo).joinedload(Modelo.marca)
        ).all()

        # 2. Renderizamos la plantilla, pasando la lista de vehículos
        return render_template('vehiculos/listado.html', vehiculos=vehiculos)

    except Exception as e:
        print(f"Error al obtener vehículos: {e}")
        # (Idealmente, aquí renderizaríamos una plantilla de error)
        return "Error al cargar la página de vehículos."

# (En el futuro, aquí irían las rutas para ABM:
# @vehiculo_bp.route('/nuevo') --> Formulario para añadir un auto
# @vehiculo_bp.route('/editar/<int:id>') --> Formulario para editar un auto
# etc.)