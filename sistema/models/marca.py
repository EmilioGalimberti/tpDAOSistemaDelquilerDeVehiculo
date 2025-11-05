# /sistema/models/marca.py
from sistema import db


class Marca(db.Model):
    __tablename__ = 'marcas'  # Nombre de la tabla

    # --- Columnas ---
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)

    # --- Relaciones ---
    # 'modelos' es un atributo virtual de Python.
    # Le dice a SQLAlchemy: "Busca en la clase 'Modelo' el atributo 'marca'".
    modelos = db.relationship('Modelo', back_populates='marca')