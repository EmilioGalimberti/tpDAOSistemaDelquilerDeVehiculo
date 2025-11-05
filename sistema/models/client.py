from sistema import db

class Client(db.Model):
    __tablename__ = 'clientes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    dni = db.Column(db.String(20), unique=True, nullable=False)
    direccion = db.Column(db.String(120))
    telefono = db.Column(db.String(20))
    email = db.Column(db.String(120), unique=True, nullable=True)

    rentals = db.relationship('Rental', back_populates='client')
