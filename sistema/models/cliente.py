# /sistema/models/cliente.py
from sistema import db

class Cliente(db.Model):
    # Nombre de tabla en español y minúsculas
    __tablename__ = 'clientes' 

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    dni = db.Column(db.String(20), unique=True, nullable=False)
    direccion = db.Column(db.String(120))
    # Nombre de columna en snake_case (estilo Python)
    numero_telefono = db.Column(db.String(20)) 
    email = db.Column(db.String(120), nullable=True, unique=True)

    # Relación bidireccional con 'Alquiler'
    alquileres = db.relationship('Alquiler', back_populates='cliente')