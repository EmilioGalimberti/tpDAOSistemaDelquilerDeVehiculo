# /sistema/controllers/marca_controller.py
from flask import Blueprint, render_template
from sistema import db
# Importamos el Modelo que vamos a usar
from sistema.models.marca import Marca

# Creamos el Blueprint para el controlador de Marcas
# 'marcas' será el nombre para registrarlo en la app
marca_bp = Blueprint('marcas', __name__)


@marca_bp.route('/')
def listar_marcas():
    """
    Esta es la ruta "index" del controlador de marcas (ej. /marcas/).
    Prueba la 'R' (Read) de nuestro CRUD.
    """
    try:
        # 1. Obtenemos todas las marcas de la BD usando el Modelo
        #    Esto es SQLAlchemy en acción: Marca.query.all()
        marcas = Marca.query.all()

        # 2. Renderizamos la plantilla HTML, pasando la lista de marcas
        return render_template('marcas/listado.html', marcas=marcas)

    except Exception as e:
        print(f"Error al obtener marcas: {e}")
        # Idealmente, aquí renderizaríamos una plantilla de error
        return "Error al cargar la página de marcas."