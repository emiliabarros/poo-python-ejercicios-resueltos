"""
Ejemplo 02 — Encapsulamiento con @property
===========================================
Concepto: controlar el acceso a atributos mediante getter y setter,
agregando validación sin cambiar la interfaz pública.

Puntos clave:
- @property convierte un método en atributo de solo lectura.
- @atributo.setter define la validación antes de asignar.
- La interfaz pública (ana.edad) NO cambia; la protección interna, sí.
"""


class Persona:
    """Persona con edad validada mediante @property."""

    def __init__(self, nombre: str, edad: int) -> None:
        """
        Inicializa la persona. La asignación de edad ya pasa por el setter.

        Args:
            nombre: Nombre completo.
            edad:   Edad en años (debe ser >= 0).
        """
        self.nombre = nombre
        self.edad   = edad      # ← llama al setter automáticamente

    # ── Getter ──────────────────────────────────────────────────────────────
    @property
    def edad(self) -> int:
        """Devuelve la edad almacenada internamente."""
        return self._edad       # _edad es el atributo interno real

    # ── Setter ──────────────────────────────────────────────────────────────
    @edad.setter
    def edad(self, valor: int) -> None:
        """Valida que la edad sea no negativa antes de asignarla."""
        if valor < 0:
            raise ValueError(f"La edad no puede ser negativa. Recibí: {valor}")
        self._edad = valor      # asignación al atributo interno

    def saludar(self) -> str:
        """Devuelve un saludo con nombre y edad."""
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

    def __str__(self) -> str:
        return f"Persona({self.nombre!r}, {self.edad} años)"


# ── Bloque de ejecución ─────────────────────────────────────────────────────
if __name__ == "__main__":
    ana = Persona("Ana", 25)

    # Lectura: usa el getter (parece un atributo normal)
    print(ana.edad)     # 25

    # Escritura: usa el setter (valida antes de asignar)
    ana.edad = 26
    print(ana.edad)     # 26

    # Acceso sin paréntesis (parece atributo, es método):
    print(ana.saludar())   # Hola, soy Ana y tengo 26 años.

    # Intento de asignar edad inválida
    print("\n--- Probando validación ---")
    try:
        ana.edad = -5
    except ValueError as e:
        print(f"Error capturado: {e}")
        # La edad NO cambia
    print(f"Edad después del intento inválido: {ana.edad}")  # sigue siendo 26
