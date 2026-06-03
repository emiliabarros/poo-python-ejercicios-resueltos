"""
Ejemplo 01 — Primera clase: Persona
=====================================
Concepto: clase básica con constructor, atributos de instancia y métodos.

Puntos clave:
- __init__ recibe self (el objeto nuevo) y los datos iniciales.
- self guarda los datos EN el objeto (self.nombre, self.edad).
- Cada objeto es INDEPENDIENTE: cambiar ana.edad no afecta a pedro.edad.
"""


class Persona:
    """Representa a una persona con nombre y edad."""

    def __init__(self, nombre: str, edad: int) -> None:
        """
        Inicializa una nueva Persona.

        Args:
            nombre: El nombre completo de la persona.
            edad:   La edad en años (entero positivo).
        """
        self.nombre = nombre   # guardamos nombre EN el objeto
        self.edad   = edad     # guardamos edad EN el objeto

    def saludar(self) -> str:
        """Devuelve un saludo con nombre y edad."""
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

    def cumplir_anios(self) -> str:
        """Incrementa la edad en 1 y devuelve un mensaje de felicitación."""
        self.edad += 1         # modificamos el ESTADO del objeto
        return f"Feliz cumpleaños {self.nombre}! Ahora tenés {self.edad} años."

    def __str__(self) -> str:
        """Representación amigable: se activa con print(persona)."""
        return f"Persona({self.nombre!r}, {self.edad} años)"


# ── Bloque de ejecución ─────────────────────────────────────────────────────
if __name__ == "__main__":
    # Creación de objetos (instancias)
    # Python llama __init__(ana, 'Ana', 25) automáticamente
    ana   = Persona("Ana",   25)
    pedro = Persona("Pedro", 30)

    # Uso de métodos
    print(ana.saludar())           # Hola, soy Ana y tengo 25 años.
    print(pedro.saludar())         # Hola, soy Pedro y tengo 30 años.

    print(ana.cumplir_anios())     # Feliz cumpleaños Ana! Ahora tenés 26 años.
    print(f"ana.edad  = {ana.edad}")    # 26  ← el objeto cambió
    print(f"pedro.edad = {pedro.edad}") # 30  ← pedro NO cambió (son independientes)

    # __str__ se activa con print()
    print(ana)    # Persona('Ana', 26 años)
