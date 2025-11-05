from sistema import db

class Rental(db.Model):
    __tablename__ = 'alquiler'

    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)
    total_cost = db.Column(db.Float)
    status = db.Column(db.String(20), nullable=False, default='Active')

    client_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('empleados.id'), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehiculos.id'), nullable=False)

    client = db.relationship('Client', back_populates='rentals')
    employee = db.relationship('Employee', back_populates='rentals')
    vehicle = db.relationship('Vehicle', back_populates='rentals')
