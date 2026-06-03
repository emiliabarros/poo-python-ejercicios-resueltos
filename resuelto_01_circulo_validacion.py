"""
Resuelto 01 — Clase Círculo con validación
==========================================
Objetivo: clase Circulo que calcula área y perímetro con validación
del radio mediante @property. Implementa __str__ y __eq__.

Conceptos aplicados:
- Encapsulamiento con @property y setter validado.
- Métodos de cálculo geométrico.
- Métodos dunder: __str__ y __eq__.
"""

import math


class Circulo:
    """
    Representa un círculo definido por su radio.

    El radio siempre es positivo. Cualquier intento de asignar
    un valor <= 0 lanza ValueError.
    """

    def __init__(self, radio: float) -> None:
        """
        Args:
            radio: Radio del círculo. Debe ser un número positivo.

        Raises:
            ValueError: Si radio <= 0.
        """
        # Usamos el setter para validar desde la misma creación
        self.radio = radio

    # ── Propiedad: radio ────────────────────────────────────────────────────
    @property
    def radio(self) -> float:
        """Devuelve el radio del círculo."""
        return self._radio

    @radio.setter
    def radio(self, valor: float) -> None:
        """Valida y asigna el radio."""
        if valor <= 0:
            raise ValueError(
                f"El radio debe ser positivo, recibí: {valor}"
            )
        self._radio = valor

    # ── Métodos de cálculo ──────────────────────────────────────────────────
    def calcular_area(self) -> float:
        """Devuelve el área del círculo: π × r²."""
        return math.pi * self._radio ** 2

    def calcular_perimetro(self) -> float:
        """Devuelve la longitud de la circunferencia: 2 × π × r."""
        return 2 * math.pi * self._radio

    def escalar(self, factor: float) -> "Circulo":
        """
        Devuelve un NUEVO círculo con el radio multiplicado por factor.
        No modifica el círculo original (inmutabilidad).
        """
        return Circulo(self._radio * factor)

    # ── Métodos dunder ──────────────────────────────────────────────────────
    def __str__(self) -> str:
        """Representación amigable para el usuario."""
        return (
            f"Círculo(radio={self._radio}) → "
            f"área={self.calcular_area():.4f}, "
            f"perímetro={self.calcular_perimetro():.4f}"
        )

    def __repr__(self) -> str:
        """Representación técnica para desarrolladores."""
        return f"Circulo({self._radio!r})"

    def __eq__(self, otro: object) -> bool:
        """Dos círculos son iguales si tienen exactamente el mismo radio."""
        if not isinstance(otro, Circulo):
            return NotImplemented
        return self._radio == otro._radio

    def __lt__(self, otro: "Circulo") -> bool:
        """Permite ordenar círculos por radio."""
        return self._radio < otro._radio


# ── Bloque de ejecución ─────────────────────────────────────────────────────
if __name__ == "__main__":
    c1 = Circulo(5)
    c2 = Circulo(3.5)

    print("--- Representación ---")
    print(c1)      # Círculo(radio=5) → área=78.5398, perímetro=31.4159
    print(c2)      # Círculo(radio=3.5) → ...
    print(repr(c1))  # Circulo(5)

    print("\n--- Cálculos ---")
    print(f"Área c1:       {c1.calcular_area():.4f}")
    print(f"Perímetro c1:  {c1.calcular_perimetro():.4f}")

    print("\n--- Comparaciones ---")
    print(f"c1 == Circulo(5): {c1 == Circulo(5)}")   # True
    print(f"c1 == c2:         {c1 == c2}")            # False
    print(f"c2 < c1:          {c2 < c1}")             # True

    print("\n--- Escalado ---")
    c3 = c1.escalar(2)
    print(f"c1 escalado x2: {c3}")
    print(f"c1 original:    {c1}")    # no cambia

    print("\n--- Validación ---")
    try:
        Circulo(-1)
    except ValueError as e:
        print(f"Error capturado: {e}")

    try:
        Circulo(0)
    except ValueError as e:
        print(f"Error capturado: {e}")
