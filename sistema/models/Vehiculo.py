# /sistema/models/vehiculo.py

from sistema.database import get_db_connection

class Vehiculo:
    """
    Representa un vehículo en el sistema.
    Esta clase manejará la lógica de negocio y la interacción
    con la tabla 'vehiculos' de la base de datos.
    """

    def __init__(self, id_modelo, anio, tipo, patente, estado, costo_diario, id=None):
        """
        Constructor para un objeto Vehiculo.
        """
        self.id = id
        self.id_modelo = id_modelo
        self.anio = anio
        self.tipo = tipo
        self.patente = patente
        self.estado = estado  # Esto será clave para el Patrón State
        self.costo_diario = costo_diario

    def guardar(self):
        """
        Guarda el vehículo actual (nuevo o existente) en la base de datos.
        """
        if self.id is None:
            # Es un vehículo nuevo (Crear)
            self._crear()
        else:
            # Es un vehículo existente (Actualizar)
            self._actualizar()

    def _crear(self):
        """Crea un nuevo vehículo en la base de datos."""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO vehiculos (id_modelo, anio, tipo, patente, estado, costo_diario)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (self.id_modelo, self.anio, self.tipo, self.patente, self.estado, self.costo_diario)
            )
            self.id = cursor.lastrowid # Obtenemos el ID auto-generado
            conn.commit()

    def _actualizar(self):
        """Actualiza un vehículo existente en la base dedatos."""
        with get_db_connection() as conn:
            conn.execute(
                """
                UPDATE vehiculos
                SET id_modelo = ?, anio = ?, tipo = ?, patente = ?, estado = ?, costo_diario = ?
                WHERE id = ?
                """,
                (self.id_modelo, self.anio, self.tipo, self.patente, self.estado, self.costo_diario, self.id)
            )
            conn.commit()

    @staticmethod
    def eliminar(id):
        """Elimina un vehículo de la base de datos por su ID."""
        with get_db_connection() as conn:
            conn.execute("DELETE FROM vehiculos WHERE id = ?", (id,))
            conn.commit()

    @staticmethod
    def obtener_por_id(id):
        """Obtiene un vehículo por su ID y devuelve un objeto Vehiculo."""
        with get_db_connection() as conn:
            fila = conn.execute("SELECT * FROM vehiculos WHERE id = ?", (id,)).fetchone()
            if fila:
                # Convertimos la fila (sqlite3.Row) en un objeto Vehiculo
                return Vehiculo(
                    id=fila['id'],
                    id_modelo=fila['id_modelo'],
                    anio=fila['anio'],
                    tipo=fila['tipo'],
                    patente=fila['patente'],
                    estado=fila['estado'],
                    costo_diario=fila['costo_diario']
                )
            return None # No se encontró

    @staticmethod
    def obtener_todos():
        """Obtiene todos los vehículos y devuelve una lista de objetos Vehiculo."""
        with get_db_connection() as conn:
            filas = conn.execute("SELECT * FROM vehiculos").fetchall()
            # Convertimos cada fila en un objeto Vehiculo
            return [
                Vehiculo(
                    id=fila['id'],
                    id_modelo=fila['id_modelo'],
                    anio=fila['anio'],
                    tipo=fila['tipo'],
                    patente=fila['patente'],
                    estado=fila['estado'],
                    costo_diario=fila['costo_diario']
                ) for fila in filas
            ]