"""
Resuelto 02 — Fracción con operadores aritméticos
==================================================
Objetivo: clase Fraccion completa con operaciones aritméticas,
simplificación automática y operadores de comparación.

Conceptos aplicados:
- Métodos dunder para operadores: __add__, __sub__, __mul__, __truediv__
- Comparación: __eq__, __lt__
- Simplificación con MCD (máximo común divisor)
- __str__ y __repr__
"""

from math import gcd


class Fraccion:
    """
    Fracción matemática irreducible con numerador y denominador enteros.

    Se simplifica automáticamente en el constructor usando el MCD.
    El denominador siempre es positivo (el signo va al numerador).
    """

    def __init__(self, num: int, den: int) -> None:
        """
        Args:
            num: Numerador (entero).
            den: Denominador (entero no nulo).

        Raises:
            ZeroDivisionError: Si den == 0.
        """
        if den == 0:
            raise ZeroDivisionError("El denominador no puede ser 0")

        # Normalizar: denominador siempre positivo
        signo  = -1 if den < 0 else 1
        factor = gcd(abs(num), abs(den))

        self.num = signo * num // factor     # numerador simplificado
        self.den = abs(den) // factor        # denominador simplificado (siempre > 0)

    # ── Operaciones aritméticas ─────────────────────────────────────────────
    def __add__(self, otra: "Fraccion") -> "Fraccion":
        """a/b + c/d = (a*d + c*b) / (b*d)"""
        return Fraccion(
            self.num * otra.den + otra.num * self.den,
            self.den * otra.den
        )

    def __sub__(self, otra: "Fraccion") -> "Fraccion":
        """a/b - c/d = (a*d - c*b) / (b*d)"""
        return Fraccion(
            self.num * otra.den - otra.num * self.den,
            self.den * otra.den
        )

    def __mul__(self, otra: "Fraccion") -> "Fraccion":
        """a/b * c/d = (a*c) / (b*d)"""
        return Fraccion(self.num * otra.num, self.den * otra.den)

    def __truediv__(self, otra: "Fraccion") -> "Fraccion":
        """a/b ÷ c/d = (a*d) / (b*c)  [multiplicar por el inverso]"""
        return Fraccion(self.num * otra.den, self.den * otra.num)

    # ── Comparaciones ───────────────────────────────────────────────────────
    def __eq__(self, otra: object) -> bool:
        """Dos fracciones son iguales si num y den simplificados coinciden."""
        if not isinstance(otra, Fraccion):
            return NotImplemented
        return self.num == otra.num and self.den == otra.den

    def __lt__(self, otra: "Fraccion") -> bool:
        """a/b < c/d  ↔  a*d < c*b  (misma lógica de denominador común)"""
        return self.num * otra.den < otra.num * self.den

    def __le__(self, otra: "Fraccion") -> bool:
        return self == otra or self < otra

    # ── Representación ──────────────────────────────────────────────────────
    def __str__(self) -> str:
        """Si el denominador es 1, muestra solo el numerador."""
        if self.den == 1:
            return str(self.num)
        return f"{self.num}/{self.den}"

    def __repr__(self) -> str:
        return f"Fraccion({self.num}, {self.den})"

    def a_decimal(self) -> float:
        """Devuelve el valor decimal de la fracción."""
        return self.num / self.den


# ── Bloque de ejecución ─────────────────────────────────────────────────────
if __name__ == "__main__":
    a = Fraccion(1, 2)   # 1/2
    b = Fraccion(1, 3)   # 1/3

    print("--- Fracciones creadas ---")
    print(f"a = {a}")    # 1/2
    print(f"b = {b}")    # 1/3

    print("\n--- Operaciones aritméticas ---")
    print(f"a + b = {a + b}")   # 5/6
    print(f"a - b = {a - b}")   # 1/6
    print(f"a * b = {a * b}")   # 1/6
    print(f"a / b = {a / b}")   # 3/2

    print("\n--- Simplificación automática ---")
    c = Fraccion(2, 4)     # debe simplificarse a 1/2
    print(f"Fraccion(2, 4)  = {c}")       # 1/2
    print(f"a == Fraccion(2, 4): {a == c}")  # True

    d = Fraccion(6, 3)     # debe simplificarse a 2 (den == 1)
    print(f"Fraccion(6, 3)  = {d}")       # 2 (sin denominador)

    print("\n--- Negativo ---")
    e = Fraccion(-3, -4)   # signo normalizado → 3/4
    print(f"Fraccion(-3, -4) = {e}")     # 3/4

    f_neg = Fraccion(3, -4)  # denominador negativo → signo al numerador
    print(f"Fraccion(3, -4)  = {f_neg}") # -3/4

    print("\n--- Comparaciones ---")
    print(f"a < a / b:  {a < (a / b)}")   # True  (1/2 < 3/2)
    print(f"b < a:      {b < a}")          # True  (1/3 < 1/2)

    print("\n--- Decimal ---")
    print(f"a como decimal: {a.a_decimal()}")   # 0.5

    print("\n--- Validación ---")
    try:
        Fraccion(1, 0)
    except ZeroDivisionError as e:
        print(f"Error capturado: {e}")
