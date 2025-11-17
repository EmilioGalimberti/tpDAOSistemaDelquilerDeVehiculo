# /sistema/controllers/main_controller.py
from flask import Blueprint, render_template
# --- ¡AÑADE ESTOS IMPORTS! ---
from sistema.models.alquiler import Alquiler
from sistema.models.vehiculo import Vehiculo
from sistema import db

# 1. Creamos el Blueprint
# 'main' es el nombre del blueprint.
# __name__ ayuda a Flask a encontrar la ubicación del blueprint.
main_bp = Blueprint('main', __name__)

# 2. Definimos la ruta dentro del Blueprint
# Nota: Ahora usamos @main_bp.route() en lugar de @app.route()
@main_bp.route('/')
@main_bp.route('/index')
def index():
    """
        Ruta principal. Ahora renderiza el dashboard con datos reales.
        """
    try:
        # --- ¡AÑADE ESTA LÓGICA DE CONSULTA! ---
        total_alquileres = Alquiler.query.count()
        vehiculos_disponibles = Vehiculo.query.filter_by(estado='Disponible').count()
        # Contamos "Ocupados" como Alquilado o En Mantenimiento
        vehiculos_ocupados = Vehiculo.query.filter(
            Vehiculo.estado.in_(['Alquilado', 'EnMantenimiento'])
        ).count()
        # ------------------------------------

        # Pasamos las variables a la plantilla
        return render_template('index.html',
                               total_alquileres=total_alquileres,
                               vehiculos_disponibles=vehiculos_disponibles,
                               vehiculos_ocupados=vehiculos_ocupados)

    except Exception as e:
        print(f"Error al cargar el dashboard: {e}")
        # Si falla, muestra el HTML estático
        return render_template('index.html',
                               total_alquileres='N/A',
                               vehiculos_disponibles='N/A',
                               vehiculos_ocupados='N/A')

# Aquí podrías agregar otras rutas "principales"
# como @main_bp.route('/about'), etc.