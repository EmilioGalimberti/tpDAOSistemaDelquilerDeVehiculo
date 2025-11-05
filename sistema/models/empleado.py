from sistema import db

class Empleado(db.Model):
    __tablename__ = 'empleados'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    dni = db.Column(db.String(20), unique=True, nullable=False)
    rol = db.Column(db.String(80), nullable=False)
    direccion = db.Column(db.String(120), nullable=True)
    telefono = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(120), nullable=True)

    alquileres = db.relationship('Alquiler', back_populates='empleado')
