# /sistema/models/alquiler.py
from sistema import db
from datetime import datetime # Importamos datetime

class Alquiler(db.Model):
    __tablename__ = 'alquiler'

    id = db.Column(db.Integer, primary_key=True)
    # Usamos DateTime para más precisión
    fecha_inicio = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 
    fecha_fin = db.Column(db.DateTime) # Permitimos que sea nulo al crear
    costo_total = db.Column(db.Float)
    estado = db.Column(db.String(20), nullable=False, default='Activo')

    # --- ¡CORRECCIÓN! Descomentamos las claves foráneas ---
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    id_empleado = db.Column(db.Integer, db.ForeignKey('empleados.id'), nullable=False)
    id_vehiculo = db.Column(db.Integer, db.ForeignKey('vehiculos.id'), nullable=False)

    # --- ¡CORRECCIÓN! Descomentamos las relaciones ---
    cliente = db.relationship('Cliente', back_populates='alquileres')
    empleado = db.relationship('Empleado', back_populates='alquileres')
    vehiculo = db.relationship('Vehiculo', back_populates='alquileres')