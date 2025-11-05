# /sistema/models/modelo.py
from sistema import db


class Modelo(db.Model):
    __tablename__ = 'modelos'

    # --- Columnas ---
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(100), nullable=False)

    # Clave Foránea: Le decimos que esta columna se conecta con 'marcas.id'
    id_marca = db.Column(db.Integer, db.ForeignKey('marcas.id'), nullable=False)

    # --- Relaciones ---
    # 'marca' es el atributo virtual para acceder al objeto Marca
    marca = db.relationship('Marca', back_populates='modelos')

    # 'vehiculos' es el atributo virtual para la lista de vehículos de este modelo
    vehiculos = db.relationship('Vehiculo', back_populates='modelo')