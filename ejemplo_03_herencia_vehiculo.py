"""
Ejemplo 03 — Herencia: Vehículo, Auto y Moto
=============================================
Concepto: crear clases hijas a partir de una clase base usando herencia.

Puntos clave:
- super().__init__(...) inicializa la parte heredada del padre.
- Las hijas pueden sobreescribir métodos del padre (override).
- Las hijas pueden agregar métodos propios que el padre no tiene.
- isinstance() devuelve True tanto para la clase propia como para la padre.
- El polimorfismo permite recorrer objetos distintos con el mismo código.
"""


class Vehiculo:
    """Clase base para cualquier vehículo motorizado."""

    def __init__(self, marca: str, modelo: str, anio: int) -> None:
        """
        Args:
            marca:  Fabricante del vehículo.
            modelo: Nombre del modelo.
            anio:   Año de fabricación.
        """
        self.marca      = marca
        self.modelo     = modelo
        self.anio       = anio
        self._velocidad = 0          # atributo protegido (estado interno)

    def acelerar(self, cantidad: int) -> str:
        """Incrementa la velocidad y devuelve el estado actual."""
        self._velocidad += cantidad
        return f"{self.marca}: {self._velocidad} km/h"

    def frenar(self, cantidad: int) -> str:
        """Reduce la velocidad (mínimo 0)."""
        self._velocidad = max(0, self._velocidad - cantidad)
        return f"{self.marca}: {self._velocidad} km/h"

    def tipo(self) -> str:
        """Descripción del tipo de vehículo. Las hijas deben sobreescribir esto."""
        return "Vehículo genérico"

    def __str__(self) -> str:
        return f"{self.marca} {self.modelo} ({self.anio})"


# ── Clase hija: Auto ────────────────────────────────────────────────────────
class Auto(Vehiculo):
    """Vehículo de cuatro ruedas con número de puertas."""

    def __init__(self, marca: str, modelo: str, anio: int, puertas: int) -> None:
        """
        Args:
            puertas: Cantidad de puertas del vehículo.
        """
        super().__init__(marca, modelo, anio)   # inicializa la parte Vehiculo
        self.puertas = puertas                   # atributo propio de Auto

    def tipo(self) -> str:
        """Sobreescritura: describe el auto con sus puertas."""
        return f"Auto de {self.puertas} puertas"

    def abrir_maletero(self) -> str:
        """Método propio de Auto, no existe en Vehiculo."""
        return f"{self.marca}: maletero abierto"


# ── Clase hija: Moto ────────────────────────────────────────────────────────
class Moto(Vehiculo):
    """Vehículo de dos ruedas con tipo de moto."""

    def __init__(self, marca: str, modelo: str, anio: int, tipo_moto: str) -> None:
        super().__init__(marca, modelo, anio)
        self.tipo_moto = tipo_moto

    def tipo(self) -> str:
        """Sobreescritura: describe la moto con su categoría."""
        return f"Moto {self.tipo_moto}"

    def hacer_caballito(self) -> str:
        """Método exclusivo de Moto."""
        return f"{self.marca}: ¡Caballito!"


# ── Bloque de ejecución ─────────────────────────────────────────────────────
if __name__ == "__main__":
    auto = Auto("Toyota", "Corolla", 2022, 4)
    moto = Moto("Honda",  "CBR",     2023, "deportiva")

    # __str__ heredado de Vehiculo
    print(auto)                         # Toyota Corolla (2022)
    print(moto)                         # Honda CBR (2023)

    # tipo() sobreescrito en cada hija
    print(auto.tipo())                  # Auto de 4 puertas
    print(moto.tipo())                  # Moto deportiva

    # Métodos heredados de Vehiculo
    print(auto.acelerar(60))            # Toyota: 60 km/h
    print(auto.frenar(20))              # Toyota: 40 km/h

    # Métodos propios de cada clase
    print(auto.abrir_maletero())        # Toyota: maletero abierto
    print(moto.hacer_caballito())       # Honda: ¡Caballito!

    # isinstance: un Auto ES UN Vehiculo también
    print(f"\nisinstance(auto, Auto):     {isinstance(auto, Auto)}")      # True
    print(f"isinstance(auto, Vehiculo): {isinstance(auto, Vehiculo)}")   # True
    print(f"isinstance(moto, Auto):     {isinstance(moto, Auto)}")       # False

    # ── Polimorfismo ─────────────────────────────────────────────────────
    print("\n--- Polimorfismo: mismo código, distintas respuestas ---")
    vehiculos = [auto, moto]
    for v in vehiculos:
        # tipo() responde diferente según la clase real del objeto
        print(f"  {v.marca}: {v.tipo()}")
