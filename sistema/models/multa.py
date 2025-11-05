from sistema import db

class Multa(db.Model):
    __tablename__ = 'multa'

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(200))
    monto = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    id_alquiler = db.Column(db.Integer, db.ForeignKey('alquiler.id'), nullable=False)

    alquiler = db.relationship('Alquiler', back_populates='multas')
