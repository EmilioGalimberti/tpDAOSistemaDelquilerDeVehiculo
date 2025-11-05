from sistema import db

class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    id_number = db.Column(db.String(20), unique=True, nullable=False)
    address = db.Column(db.String(120))
    telephone_number = db.Column(db.String(20))
    email = db.Column(db.String(120), nullable=True)

    # The relationship to 'Rental' is commented out until the Rental model is created.
    # rentals = db.relationship('Rental', back_populates='client')
