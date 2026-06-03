"""
Ejemplo 05 — Composición y Agregación: Pedido de Restaurant
=============================================================
Concepto: diferencia entre composición (◆) y agregación (◇).

- Composición (◆): Pedido CREA sus Items internamente.
  Los Items no tienen sentido sin el Pedido que los contiene.
  Si el Pedido desaparece, los Items también.

- Agregación (◇): Mesa RECIBE Pedidos creados desde afuera.
  Los Pedidos pueden existir sin la Mesa.
  Si la Mesa desaparece, los Pedidos siguen vivos.
"""

from typing import List


# ── Parte de Pedido (composición ◆) ─────────────────────────────────────────
class ItemPedido:
    """Representa un ítem individual dentro de un pedido."""

    def __init__(self, nombre: str, precio: float, cantidad: int = 1) -> None:
        """
        Args:
            nombre:   Nombre del producto.
            precio:   Precio unitario.
            cantidad: Cantidad solicitada (por defecto 1).
        """
        self.nombre   = nombre
        self.precio   = precio
        self.cantidad = cantidad

    def subtotal(self) -> float:
        """Calcula el costo total de este ítem."""
        return self.precio * self.cantidad

    def __str__(self) -> str:
        return f"{self.nombre} x{self.cantidad} = ${self.subtotal():.2f}"


# ── Contiene Items por composición (◆) ──────────────────────────────────────
class Pedido:
    """
    Pedido de un cliente. CREA sus ítems internamente (composición).
    Lleva un contador de clase para asignar números únicos.
    """

    _contador: int = 0      # atributo de CLASE: compartido por todos los pedidos

    def __init__(self, cliente: str) -> None:
        """
        Args:
            cliente: Nombre del cliente que realiza el pedido.
        """
        Pedido._contador += 1
        self.numero  = Pedido._contador
        self.cliente = cliente
        # Los Items nacen DENTRO del pedido → composición ◆
        self._items: List[ItemPedido] = []

    def agregar(self, nombre: str, precio: float, cantidad: int = 1) -> None:
        """Agrega un ítem al pedido creándolo internamente."""
        self._items.append(ItemPedido(nombre, precio, cantidad))

    def total(self) -> float:
        """Suma los subtotales de todos los ítems."""
        return sum(item.subtotal() for item in self._items)

    def __str__(self) -> str:
        if not self._items:
            return f"Pedido #{self.numero} ({self.cliente}): [vacío]"
        detalle = "\n  ".join(str(item) for item in self._items)
        return (
            f"Pedido #{self.numero} ({self.cliente}):\n"
            f"  {detalle}\n"
            f"  TOTAL: ${self.total():.2f}"
        )


# ── Agrega Pedidos por agregación (◇) ────────────────────────────────────────
class Mesa:
    """
    Mesa del restaurant. RECIBE pedidos creados desde afuera (agregación ◇).
    Si la mesa desaparece, los pedidos siguen existiendo.
    """

    def __init__(self, numero: int) -> None:
        self.numero   = numero
        # Los Pedidos se crean AFUERA y se pasan aquí → agregación ◇
        self._pedidos: List[Pedido] = []

    def tomar_pedido(self, pedido: Pedido) -> None:
        """Registra un pedido ya creado en la mesa."""
        self._pedidos.append(pedido)

    def cuenta_total(self) -> float:
        """Suma los totales de todos los pedidos de la mesa."""
        return sum(p.total() for p in self._pedidos)

    def __str__(self) -> str:
        return (
            f"Mesa {self.numero} — "
            f"{len(self._pedidos)} pedido(s) — "
            f"Total: ${self.cuenta_total():.2f}"
        )


# ── Bloque de ejecución ─────────────────────────────────────────────────────
if __name__ == "__main__":
    # Creamos pedidos (AFUERA de la mesa → agregación)
    p1 = Pedido("Ana")
    p1.agregar("Milanesa", 1200, 1)
    p1.agregar("Gaseosa",   300, 2)

    p2 = Pedido("Carlos")
    p2.agregar("Pizza",    1500, 1)
    p2.agregar("Agua",      150, 2)

    # Los pedidos existen independientemente de la mesa
    print("--- Pedidos individuales ---")
    print(p1)
    print()
    print(p2)

    # La mesa los AGREGA (no los crea)
    mesa_5 = Mesa(5)
    mesa_5.tomar_pedido(p1)
    mesa_5.tomar_pedido(p2)

    print("\n--- Cuenta de la mesa ---")
    print(mesa_5)

    # Demostración de que los pedidos sobreviven si la mesa se elimina
    del mesa_5
    print("\n--- Después de borrar la mesa ---")
    print(f"p1 (Ana) sigue vivo: {p1.cliente}")    # Ana ← sobrevive
    print(f"p2 (Carlos) sigue vivo: {p2.cliente}") # Carlos ← sobrevive
