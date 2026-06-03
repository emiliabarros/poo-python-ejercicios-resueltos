"""
Resuelto 03 — Jerarquía Animal con Clases Abstractas
=====================================================
Objetivo: clase abstracta Animal con subclases concretas que implementan
comportamientos propios usando ABC y @abstractmethod.

Conceptos aplicados:
- Clases abstractas (ABC) como contratos obligatorios.
- Métodos abstractos que las subclases DEBEN implementar.
- super() para extender métodos del padre.
- Polimorfismo: describirse() responde diferente según la subclase.
"""

from abc import ABC, abstractmethod


# ── Clase abstracta (contrato) ───────────────────────────────────────────────
class Animal(ABC):
    """
    Clase base abstracta para cualquier animal.

    No puede instanciarse directamente. Obliga a las subclases a
    implementar emitir_sonido() y tipo_alimentacion().
    """

    def __init__(self, nombre: str, peso: float) -> None:
        """
        Args:
            nombre: Nombre del animal.
            peso:   Peso en kilogramos.
        """
        self.nombre = nombre
        self.peso   = peso

    @abstractmethod
    def emitir_sonido(self) -> str:
        """Devuelve el sonido característico del animal."""
        pass

    @abstractmethod
    def tipo_alimentacion(self) -> str:
        """Devuelve 'carnívoro', 'herbívoro' u 'omnívoro'."""
        pass

    def describirse(self) -> str:
        """
        Descripción general del animal.
        Las subclases pueden extender este método con super().
        """
        return (
            f"{type(self).__name__} [{self.nombre}] "
            f"| {self.peso} kg "
            f"| {self.tipo_alimentacion()} "
            f"| dice: {self.emitir_sonido()}"
        )


# ── Subclases concretas ──────────────────────────────────────────────────────
class Perro(Animal):
    """Perro doméstico con raza."""

    def __init__(self, nombre: str, peso: float, raza: str) -> None:
        super().__init__(nombre, peso)
        self.raza = raza

    def emitir_sonido(self) -> str:
        return "¡Guau!"

    def tipo_alimentacion(self) -> str:
        return "omnívoro"

    def describirse(self) -> str:
        """Extiende la descripción del padre agregando la raza."""
        base = super().describirse()
        return base + f" | raza: {self.raza}"

    def buscar_pelota(self) -> str:
        """Comportamiento exclusivo del Perro."""
        return f"{self.nombre} busca la pelota!"


class Gato(Animal):
    """Gato doméstico."""

    def emitir_sonido(self) -> str:
        return "¡Miau!"

    def tipo_alimentacion(self) -> str:
        return "carnívoro"

    def ronronear(self) -> str:
        """Comportamiento exclusivo del Gato."""
        return f"{self.nombre}: Prrrrr..."


class Aguila(Animal):
    """Águila con envergadura de alas."""

    def __init__(self, nombre: str, peso: float, envergadura: float) -> None:
        """
        Args:
            envergadura: Apertura alar en metros.
        """
        super().__init__(nombre, peso)
        self.envergadura = envergadura

    def emitir_sonido(self) -> str:
        return "¡Kree!"

    def tipo_alimentacion(self) -> str:
        return "carnívoro"

    def describirse(self) -> str:
        """Extiende la descripción con la envergadura."""
        base = super().describirse()
        return base + f" | envergadura: {self.envergadura} m"

    def volar(self) -> str:
        """Comportamiento exclusivo del Águila."""
        return f"{self.nombre} despega con {self.envergadura} m de alas"


# ── Bloque de ejecución ─────────────────────────────────────────────────────
if __name__ == "__main__":
    # No se puede instanciar la clase abstracta
    try:
        Animal("X", 10)
    except TypeError as e:
        print(f"Error esperado: {e}\n")

    # Crear animales concretos
    animales = [
        Perro("Rex",      25.0, "Labrador"),
        Gato("Michi",      4.0),
        Aguila("Libertad", 6.0, 2.2),
    ]

    print("--- Polimorfismo: describirse() ---")
    for a in animales:
        print(f"  {a.describirse()}")

    print("\n--- Métodos exclusivos ---")
    rex     = animales[0]
    michi   = animales[1]
    libertad = animales[2]

    # Solo Perro tiene buscar_pelota
    print(rex.buscar_pelota())

    # Solo Gato tiene ronronear
    print(michi.ronronear())

    # Solo Águila tiene volar
    print(libertad.volar())

    print("\n--- isinstance ---")
    print(f"rex ES UN Animal: {isinstance(rex, Animal)}")       # True
    print(f"rex ES UN Gato:   {isinstance(rex, Gato)}")         # False
