# /sistema/models/estado_vehiculo.py
from abc import ABC, abstractmethod


#aca ver como lo coluciona pero nostros en dsi por ejemplo lo hacemos diferente le pasamos el contexto
# por parametro del metodo que le cambia el estado o haga algo segun el estado, y despues llamara al contexto.setEstado
#En este caso lo hacemos con el metodo setContext y lo tenemos como attr
class EstadoVehiculo(ABC):
    """
    La Interfaz (Clase Abstracta) para el Patrón State.
    Define los métodos que todos los estados concretos deben implementar.
    El 'contexto' (el Vehiculo) llamará a estos métodos.
    """

    def __init__(self):
        # El 'context' será el objeto Vehiculo
        self.context = None

    def set_context(self, context):
        """
        Asigna el objeto Vehiculo (contexto) a este estado
        para que el estado pueda manipularlo.
        """
        self.context = context

    @abstractmethod
    def alquilar(self):
        """Intenta alquilar el vehículo."""
        pass

    @abstractmethod
    def devolver(self):
        """Intenta devolver el vehículo."""
        pass

    @abstractmethod
    def enviar_a_mantenimiento(self):
        """Pone el vehículo en mantenimiento."""
        pass

    @abstractmethod
    def sacar_de_mantenimiento(self):
        """Devuelve el vehículo a 'Disponible'."""
        pass


# --- Estados Concretos ---

class EstadoDisponible(EstadoVehiculo):
    """El estado 'Disponible'."""

    def alquilar(self):
        #Esta es la transición válida.
        print("Vehículo alquilado. Pasando a estado 'Alquilado'.")
        # El estado le dice al contexto (Vehiculo) que cambie.
        self.context.set_estado(EstadoAlquilado())

    def devolver(self):
        print("ERROR: No se puede devolver un vehículo que ya está disponible.")
        raise Exception("Operación no válida para el estado 'Disponible'")

    def enviar_a_mantenimiento(self):
        print("Vehículo enviado a mantenimiento. Pasando a 'En Mantenimiento'.")
        self.context.set_estado(EstadoEnMantenimiento())

    def sacar_de_mantenimiento(self):
        print("ERROR: El vehículo ya está disponible.")
        raise Exception("Operación no válida para el estado 'Disponible'")


# ---
class EstadoAlquilado(EstadoVehiculo):
    """El estado 'Alquilado'."""

    def alquilar(self):
        print("ERROR: El vehículo ya está alquilado.")
        raise Exception("Operación no válida para el estado 'Alquilado'")

    def devolver(self):
        # ¡ÉXITO! Esta es la transición válida.
        print("Vehículo devuelto. Pasando a estado 'Disponible'.")
        self.context.set_estado(EstadoDisponible())

    def enviar_a_mantenimiento(self):
        print("ERROR: No se puede enviar a mantenimiento un vehículo alquilado.")
        raise Exception("Operación no válida para el estado 'Alquilado'")

    def sacar_de_mantenimiento(self):
        print("ERROR: El vehículo está alquilado, no en mantenimiento.")
        raise Exception("Operación no válida para el estado 'Alquilado'")


# ---
class EstadoEnMantenimiento(EstadoVehiculo):
    """El estado 'En Mantenimiento'."""

    def alquilar(self):
        print("ERROR: El vehículo está en mantenimiento.")
        raise Exception("Operación no válida para el estado 'En Mantenimiento'")

    def devolver(self):
        print("ERROR: No se puede devolver un vehículo que está en mantenimiento.")
        raise Exception("Operación no válida para el estado 'En Mantenimiento'")

    def enviar_a_mantenimiento(self):
        print("ERROR: El vehículo ya está en mantenimiento.")
        raise Exception("OperGoperación no válida para el estado 'En Mantenimiento'")

    def sacar_de_mantenimiento(self):
        # ¡ÉXITO! Esta es la transición válida.
        print("Vehículo reparado. Pasando a estado 'Disponible'.")
        self.context.set_estado(EstadoDisponible())