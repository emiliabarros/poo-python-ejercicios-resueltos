"""
Resuelto 06 — De Diagrama UML a Código Python
==============================================
Objetivo: implementar fielmente el siguiente diagrama UML en Python.

DIAGRAMA UML:
─────────────────────────────────────────────────────
  «abstract»
 ┌─────────────────────┐
 │      Empleado       │
 ├─────────────────────┤
 │ + nombre: str       │
 │ # _salario: float   │
 ├─────────────────────┤
 │ + calcular_bono()   │  ← abstracto
 │ + __str__(): str    │
 └──────────┬──────────┘
            │ ▲ (herencia)
   ┌─────────┴─────────┐
   │                   │
┌──┴──────┐      ┌─────┴───────────┐
│ Vendedor│      │    Gerente      │
├─────────┤      ├─────────────────┤
│+ventas  │      │ + tam_equipo    │
├─────────┤      ├─────────────────┤
│+calc_   │      │ + calcular_bono │
│  bono() │      └─────────────────┘
└─────────┘
─────────────────────────────────────────────────────

Reglas de negocio:
- Vendedor: bono = 5% de las ventas del mes.
- Gerente:  bono = 10% del salario + $500 por miembro del equipo.

Conceptos aplicados:
- Lectura e implementación de diagramas UML.
- Clases abstractas con ABC.
- Herencia y polimorfismo.
- Visibilidad: público (+), protegido (#).
"""

from abc import ABC, abstractmethod
from typing import List


# ── Clase abstracta: Empleado ────────────────────────────────────────────────
class Empleado(ABC):
    """
    Clase abstracta que modela a cualquier empleado de la empresa.
    Toda subclase DEBE implementar calcular_bono().

    UML:
      + nombre: str       → atributo público
      # _salario: float   → atributo protegido
    """

    def __init__(self, nombre: str, salario: float) -> None:
        """
        Args:
            nombre:  Nombre completo del empleado.
            salario: Salario mensual base (debe ser positivo).

        Raises:
            ValueError: Si el salario es negativo.
        """
        if salario < 0:
            raise ValueError("El salario no puede ser negativo")
        self.nombre    = nombre       # + público
        self._salario  = salario      # # protegido

    @abstractmethod
    def calcular_bono(self) -> float:
        """Calcula el bono mensual. Cada subclase define su fórmula."""
        pass

    def __str__(self) -> str:
        """Formato uniforme para todos los empleados."""
        return (
            f"{type(self).__name__:10} | "
            f"{self.nombre:15} | "
            f"Salario: ${self._salario:>10,.0f} | "
            f"Bono: ${self.calcular_bono():>8,.0f}"
        )


# ── Subclase: Vendedor ────────────────────────────────────────────────────────
class Vendedor(Empleado):
    """
    Empleado de ventas con comisión proporcional a sus ventas.
    Bono = 5% de ventas_mes.

    UML: + ventas_mes: float
    """

    def __init__(self, nombre: str, salario: float, ventas_mes: float) -> None:
        """
        Args:
            ventas_mes: Monto total vendido en el mes.
        """
        super().__init__(nombre, salario)
        self.ventas_mes = ventas_mes

    def calcular_bono(self) -> float:
        """5% de las ventas del mes."""
        return self.ventas_mes * 0.05


# ── Subclase: Gerente ────────────────────────────────────────────────────────
class Gerente(Empleado):
    """
    Gerente con equipo a cargo.
    Bono = 10% del salario + $500 por miembro del equipo.

    UML: + tam_equipo: int
    """

    def __init__(self, nombre: str, salario: float, tam_equipo: int) -> None:
        """
        Args:
            tam_equipo: Cantidad de personas a cargo.
        """
        super().__init__(nombre, salario)
        self.tam_equipo = tam_equipo

    def calcular_bono(self) -> float:
        """10% del salario base + $500 por cada miembro del equipo."""
        bono_base  = self._salario * 0.10
        bono_extra = self.tam_equipo * 500
        return bono_base + bono_extra


# ── Función auxiliar ────────────────────────────────────────────────────────
def liquidacion_mensual(empleados: List[Empleado]) -> None:
    """Imprime el resumen de liquidación de un listado de empleados."""
    print(f"{'Tipo':<10} | {'Nombre':<15} | {'Salario':>18} | {'Bono':>14}")
    print("-" * 68)
    total_bonos = 0.0
    for e in empleados:
        print(f"  {e}")
        total_bonos += e.calcular_bono()
    print("-" * 68)
    print(f"{'Total bonos:':>52} ${total_bonos:>8,.0f}")


# ── Bloque de ejecución ─────────────────────────────────────────────────────
if __name__ == "__main__":
    empleados: List[Empleado] = [
        Vendedor("Ana López",   50_000, 200_000),
        Vendedor("Luis García", 50_000,  80_000),
        Vendedor("María Paz",   45_000, 150_000),
        Gerente("Laura Torres", 80_000, 5),
        Gerente("Martín Díaz",  90_000, 8),
    ]

    print("=== LIQUIDACIÓN MENSUAL ===\n")
    liquidacion_mensual(empleados)

    # Polimorfismo en acción
    print("\n--- Solo los vendedores que superaron $100k en ventas ---")
    top_vendedores = [
        e for e in empleados
        if isinstance(e, Vendedor) and e.ventas_mes > 100_000
    ]
    for v in top_vendedores:
        print(f"  {v.nombre}: ventas ${v.ventas_mes:,.0f}")
