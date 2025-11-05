# /sistema/models/vehiculo.py
from sistema import db


# NOTA: quitamos 'get_db_connection' y todo el SQL manual

class Vehiculo(db.Model):
    """
    Refactor de la clase Vehiculo para usar SQLAlchemy.
    La herencia de 'db.Model' nos da todo el poder del ORM.
    Ya no necesitamos métodos CRUD manuales.
    """
    __tablename__ = 'vehiculos'

    # --- Columnas (Mapeo de la tabla) ---
    id = db.Column(db.Integer, primary_key=True)
    anio = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    patente = db.Column(db.String(10), unique=True, nullable=False)
    estado = db.Column(db.String(50), default='Disponible', nullable=False)
    costo_diario = db.Column(db.Float, nullable=False)

    # Clave Foránea: Conecta con 'modelos.id'
    id_modelo = db.Column(db.Integer, db.ForeignKey('modelos.id'), nullable=False)

    # --- Relaciones (Atributos virtuales de Python) ---

    # 'modelo': Nos permite hacer 'mi_auto.modelo' y obtener el objeto Modelo
    modelo = db.relationship('Modelo', back_populates='vehiculos')

    # 'alquileres': Nos permite hacer 'mi_auto.alquileres' y obtener una
    # lista de todos los objetos Alquiler de este auto.
    alquileres = db.relationship('Alquiler', back_populates='vehiculo')

    def __repr__(self):
        # Un método útil para debugging
        return f'<Vehiculo {self.patente} (ID: {self.id})>'

    #
    # --- ¡FIN! ---
    #
    # ¿Dónde están guardar(), eliminar(), obtener_por_id()?
    # ¡YA NO LOS NECESITAMOS!
    #
    # SQLAlchemy nos los da:
    #
    # Crear:
    #   auto = Vehiculo(patente='AA123BB', ...)
    #   db.session.add(auto)
    #   db.session.commit()
    #
    # Buscar:
    #   auto = Vehiculo.query.get(1)
    #
    # Actualizar:
    #   auto.estado = 'Alquilado'
    #   db.session.commit()
    #
    # Eliminar:
    #   db.session.delete(auto)
    #   db.session.commit()
    #