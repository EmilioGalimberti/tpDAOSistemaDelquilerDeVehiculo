# /sistema/models/vehiculo.py
from sqlalchemy.orm import reconstructor
from sistema import db
from sistema.models.estado_vehiculo import EstadoDisponible, EstadoAlquilado, EstadoEnMantenimiento


# NOTA: quitamos 'get_db_connection' y todo el SQL manual

class Vehiculo(db.Model):
    """
    Refactor de la clase Vehiculo para usar SQLAlchemy.
    La herencia de 'db.Model' nos da todo el poder del ORM.
    Ya no necesitamos métodos CRUD manuales.
    """
    __tablename__ = 'vehiculos'

    # --- Columnas (Mapeo de la tabla) ---
    id = db.Column(db.Integer, primary_key=True)
    anio = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    patente = db.Column(db.String(10), unique=True, nullable=False)
    costo_diario = db.Column(db.Float, nullable=False)

    # ---Lógica del Patrón State ---
    # Columna 'estado' (la que se guarda en la BD)
    # Es un string: "Disponible", "Alquilado", "EnMantenimiento"
    estado = db.Column(db.String(50), default='Disponible', nullable=False)


    # Clave Foránea: Conecta con 'modelos.id'
    id_modelo = db.Column(db.Integer, db.ForeignKey('modelos.id'), nullable=False)

    # --- Relaciones (Atributos virtuales de Python) ---
    # 'modelo': Nos permite hacer 'mi_auto.modelo' y obtener el objeto Modelo
    modelo = db.relationship('Modelo', back_populates='vehiculos')
    # 'alquileres': Nos permite hacer 'mi_auto.alquileres' y obtener una
    # lista de todos los objetos Alquiler de este auto.
    alquileres = db.relationship('Alquiler', back_populates='vehiculo')
    mantenimientos = db.relationship('Mantenimiento', back_populates='vehiculo')


    #En esta clase debemos redefinir el constructor para que funcione con SQLALchemy y el Patron STATE
    def __init__(self, **kwargs):
        """
        Constructor para *nuevos* vehículos (cuando los creamos en Python).
        """
        super(Vehiculo, self).__init__(**kwargs)
        # Inicializa el estado por primera vez
        self._init_estado()

    @reconstructor
    def _init_estado_on_load(self):
        """
        Se ejecuta automáticamente cuando SQLAlchemy carga un Vehiculo
        desde la base de datos (ej. Vehiculo.query.get(1)).
        """
        self._init_estado()

    def _init_estado(self):
        """
        Factory de Estado: Lee el string 'self.estado' de la BD
        y crea el objeto de estado (POO) correspondiente.
        """
        if self.estado == 'Disponible':
            self._estado_actual = EstadoDisponible()
        elif self.estado == 'Alquilado':
            self._estado_actual = EstadoAlquilado()
        elif self.estado == 'EnMantenimiento':
            self._estado_actual = EstadoEnMantenimiento()
        else:
            # Fallback por si hay datos corruptos
            self._estado_actual = EstadoDisponible()

            # Le pasamos el 'Vehiculo' (self) al objeto de estado
        self._estado_actual.set_context(self)

    def set_estado(self, nuevo_estado_obj):
        """
        Method llamado por los objetos de estado para realizar la transición.
        """
        # 1. Actualiza el objeto de estado en memoria (POO)
        self._estado_actual = nuevo_estado_obj

        # 2. Actualiza el string de estado para la Base de Datos
        #    Obtenemos el nombre de la clase, ej: "EstadoDisponible"
        #    y lo simplificamos a "Disponible"
        nombre_clase = nuevo_estado_obj.__class__.__name__
        if nombre_clase.startswith("Estado"):
            self.estado = nombre_clase[6:]  # Quita "Estado"
        else:
            self.estado = nombre_clase

        print(f"Vehículo {self.patente} cambió su estado en BD a: {self.estado}")

        # --- 3. Métodos Públicos (Delegación) ---
        # La clase Vehiculo ya no tiene 'if/else', solo delega.

    def alquilar(self):
        """Intenta alquilar el vehículo."""
        try:
            self._estado_actual.alquilar()
        except Exception as e:
            print(f"Intento de ALQUILAR rechazado: {e}")
            raise  # Re-lanza la excepción para que el controlador la vea

    def devolver(self):
        """Intenta devolver el vehículo."""
        try:
            self._estado_actual.devolver()
        except Exception as e:
            print(f"Intento de DEVOLVER rechazado: {e}")
            raise

    def enviar_a_mantenimiento(self):
        """Envía el vehículo a mantenimiento."""
        try:
            self._estado_actual.enviar_a_mantenimiento()
        except Exception as e:
            print(f"Intento de MANTENIMIENTO rechazado: {e}")
            raise

    def sacar_de_mantenimiento(self):
        """Saca el vehículo de mantenimiento."""
        try:
            self._estado_actual.sacar_de_mantenimiento()
        except Exception as e:
            print(f"Intento de SACAR DE MANTENIMIENTO rechazado: {e}")
            raise

    def __repr__(self):
        return f'<Vehiculo {self.patente} (Estado: {self.estado})>'

    #
    # --- ¡FIN! ---
    #
    # ¿Dónde están guardar(), eliminar(), obtener_por_id()?
    # ¡YA NO LOS NECESITAMOS!
    #
    # SQLAlchemy nos los da:
    #
    # Crear:
    #   auto = Vehiculo(patente='AA123BB', ...)
    #   db.session.add(auto)
    #   db.session.commit()
    #
    # Buscar:
    #   auto = Vehiculo.query.get(1)
    #
    # Actualizar:
    #   auto.estado = 'Alquilado'
    #   db.session.commit()
    #
    # Eliminar:
    #   db.session.delete(auto)
    #   db.session.commit()

