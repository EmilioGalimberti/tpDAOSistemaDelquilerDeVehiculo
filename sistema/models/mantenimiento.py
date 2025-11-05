from sistema import db

class Mantenimiento(db.Model):
    __tablename__ = 'mantenimiento'

    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    descripcion = db.Column(db.String(200))
    costo = db.Column(db.Float)
    tipo = db.Column(db.String(50))
    id_vehiculo = db.Column(db.Integer, db.ForeignKey('vehiculos.id'), nullable=False)

    vehiculo = db.relationship('Vehiculo', back_populates='mantenimientos')
