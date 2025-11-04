# /sistema/controllers/main_controller.py
from flask import Blueprint, render_template

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
    Ruta principal. Renderiza la plantilla 'index.html'.
    """
    return render_template('index.html', titulo='Página Principal')

# Aquí podrías agregar otras rutas "principales"
# como @main_bp.route('/about'), etc.