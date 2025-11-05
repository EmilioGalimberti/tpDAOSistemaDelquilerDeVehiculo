# /sistema/models/__init__.py

# Este archivo convierte la carpeta 'models' en un paquete
# e importa todos los archivos de modelo.

# Esto asegura que SQLAlchemy "descubra"
# todas nuestras clases de modelo (Modelo, Vehiculo, etc.)
# cuando se cargue el paquete.

from . import marca
from . import modelo
from . import vehiculo
from . import cliente
from . import empleado
from . import alquiler

# (Cuando Jules termine, también añadirás:)
# from . import mantenimiento
# from . import multa