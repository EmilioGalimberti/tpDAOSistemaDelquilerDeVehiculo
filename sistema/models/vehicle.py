from sistema import db

class Vehicle(db.Model):
    __tablename__ = 'vehiculos'

    id = db.Column(db.Integer, primary_key=True)
    rentals = db.relationship('Rental', back_populates='vehicle')
