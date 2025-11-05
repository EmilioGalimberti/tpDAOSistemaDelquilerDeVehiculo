from sistema import db

class Cliente(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    dni = db.Column(db.String(20), unique=True, nullable=False)
    direccion = db.Column(db.String(120))
    numero_de_telefono = db.Column(db.String(20))
    email = db.Column(db.String(120), nullable=True)

    # The relationship to 'Rental' is commented out until the Rental model is created.
    # rentals = db.relationship('Rental', back_populates='client')
