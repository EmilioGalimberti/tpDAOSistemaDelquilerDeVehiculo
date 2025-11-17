# /sistema/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# 1. Crea la instancia de SQLAlchemy SIN ligarla a una app
#    Esto nos permite importarla en otros archivos (como los modelos)
#    de forma segura.
db = SQLAlchemy()


def create_app():
    """
    Función "Factory" para crear la instancia de la aplicación Flask.
    """
    app = Flask(__name__)

    # --- Configuración de la Base de Datos ---
    # Obtenemos la ruta absoluta de la raíz del proyecto
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Definimos la URI de la base de datos SQLite
    DB_PATH = os.path.join(BASE_DIR, 'alquileres.db')

    # ... (Configuración de la Base de Datos) ...
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desactiva notificaciones innecesarias

    # Necesaria para que funcionen las 'flash messages' y las sesiones
    app.config['SECRET_KEY'] = 'un-valor-secreto-muy-dificil-de-adivinar'

    # 2. Inicializa la instancia 'db' CON la aplicación 'app'
    db.init_app(app)

    # --- Registro de Blueprints (Controladores) ---
    # Usamos 'with app.app_context()' para que los blueprints
    # tengan acceso a la aplicación configurada.
    with app.app_context():
        from .controllers.main_controller import main_bp
        app.register_blueprint(main_bp)



        # Aquí registraremos los futuros blueprints
        # from .controllers.vehiculo_controller import vehiculo_bp
        # app.register_blueprint(vehiculo_bp, url_prefix='/vehiculos')

        from .controllers.marca_controller import marca_bp
        # Todas las rutas de este blueprint empezarán con /marcas
        app.register_blueprint(marca_bp, url_prefix='/marcas')

        from .controllers.vehiculo_controller import  vehiculo_bp
        app.register_blueprint(vehiculo_bp, url_prefix='/vehiculos')

        from .controllers.alquiler_controller import alquiler_bp
        app.register_blueprint(alquiler_bp, url_prefix='/alquiler')

    return app