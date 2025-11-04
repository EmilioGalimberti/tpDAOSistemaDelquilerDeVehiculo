# /sistema/__init__.py
from flask import Flask

# Crea la instancia de la aplicación Flask
app = Flask(__name__)

# --- Registro de Blueprints (Controladores) ---

# 1. Importa tu blueprint (controlador)
from .controllers.main_controller import main_bp

# 2. Registry el blueprint en la aplicación
app.register_blueprint(main_bp)

# Cuando crees el controlador de vehículos, harás lo mismo:
# from .controllers.vehiculo_controller import vehiculo_bp
# app.register_blueprint(vehiculo_bp, url_prefix='/vehiculos')
# (El url_prefix es genial para que todas las rutas de ese
#  controlador empiecen con /vehiculos)

# --- Fin del Registro ---