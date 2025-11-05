from sistema import db

class Employee(db.Model):
    __tablename__ = 'empleados'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    dni = db.Column(db.String(20), unique=True, nullable=False)
    rol = db.Column(db.String(80), nullable=False)

    rentals = db.relationship('Rental', back_populates='employee')
