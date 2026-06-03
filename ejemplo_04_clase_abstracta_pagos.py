"""
Ejemplo 04 — Clase abstracta: Sistema de Pagos
===============================================
Concepto: usar ABC (Abstract Base Class) para definir un contrato que
todas las formas de pago deben cumplir.

Puntos clave:
- Una clase abstracta NO puede instanciarse directamente.
- @abstractmethod obliga a las subclases a implementar ese método.
- Si una subclase no implementa todos los métodos abstractos → TypeError.
- Polimorfismo: cada clase concreta implementa procesar() a su manera.
"""

from abc import ABC, abstractmethod
from datetime import date


# ── Clase abstracta (contrato) ───────────────────────────────────────────────
class Pago(ABC):
    """
    Clase abstracta base para cualquier forma de pago.
    Define el contrato: toda subclase DEBE implementar procesar().
    """

    def __init__(self, monto: float) -> None:
        """
        Args:
            monto: Importe del pago. Debe ser positivo.

        Raises:
            ValueError: Si el monto es <= 0.
        """
        if monto <= 0:
            raise ValueError(f"El monto debe ser positivo, recibí: {monto}")
        self.monto = monto
        self.fecha = date.today()    # se registra automáticamente

    @abstractmethod
    def procesar(self) -> str:
        """
        Procesa el pago según el medio elegido.
        Las subclases DEBEN implementar este método.
        """
        pass    # sin implementación en la clase abstracta

    def __str__(self) -> str:
        """Representación común para todos los pagos."""
        return f"Pago de ${self.monto:.2f} el {self.fecha}"


# ── Subclase: Pago en efectivo ───────────────────────────────────────────────
class PagoEfectivo(Pago):
    """Pago realizado con dinero en efectivo."""

    def procesar(self) -> str:
        return f"Cobrado ${self.monto:.2f} en efectivo"


# ── Subclase: Pago con tarjeta ───────────────────────────────────────────────
class PagoTarjeta(Pago):
    """Pago realizado con tarjeta de crédito o débito."""

    def __init__(self, monto: float, nro_tarjeta: str) -> None:
        """
        Args:
            nro_tarjeta: Número completo de la tarjeta (se muestra solo el final).
        """
        super().__init__(monto)
        self._nro = nro_tarjeta      # guardamos el número (protegido)

    def procesar(self) -> str:
        ultimos_4 = self._nro[-4:]   # solo mostramos los últimos 4 dígitos
        return f"Cobrado ${self.monto:.2f} a tarjeta terminada en {ultimos_4}"


# ── Subclase: Pago por transferencia ────────────────────────────────────────
class PagoTransferencia(Pago):
    """Pago realizado mediante transferencia bancaria."""

    def __init__(self, monto: float, cbu: str) -> None:
        """
        Args:
            cbu: Clave Bancaria Uniforme del destinatario.
        """
        super().__init__(monto)
        self.cbu = cbu

    def procesar(self) -> str:
        ultimos = self.cbu[-4:]
        return f"Transferencia de ${self.monto:.2f} a CBU ****{ultimos}"


# ── Bloque de ejecución ─────────────────────────────────────────────────────
if __name__ == "__main__":
    # No se puede instanciar la clase abstracta directamente
    try:
        p = Pago(100)
    except TypeError as e:
        print(f"Error esperado: {e}\n")

    # Creamos distintos tipos de pago concretos
    pagos = [
        PagoEfectivo(500),
        PagoTarjeta(1200, "4111111111111234"),
        PagoTransferencia(3000, "0000003100012345678901"),
    ]

    print("--- Procesando pagos ---")
    for pago in pagos:
        # Polimorfismo: procesar() responde diferente según el tipo real
        print(f"  {pago.procesar()}")
        print(f"  {pago}")       # __str__ heredado de Pago
        print()

    # Validación de monto inválido
    print("--- Probando validación de monto ---")
    try:
        PagoEfectivo(-100)
    except ValueError as e:
        print(f"Error capturado: {e}")
