from sistema import db

class Vehiculo(db.Model):
    __tablename__ = 'vehiculos'

    id = db.Column(db.Integer, primary_key=True)
    id_modelo = db.Column(db.Integer, db.ForeignKey('modelos.id'), nullable=False)
    anio = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    patente = db.Column(db.String(20), unique=True, nullable=False)
    estado = db.Column(db.String(50), nullable=False, default='Disponible')
    costo_diario = db.Column(db.Float, nullable=False)

    alquileres = db.relationship('Alquiler', back_populates='vehiculo')
    mantenimientos = db.relationship('Mantenimiento', back_populates='vehiculo')
