"""
=============================================================
 MODELO: Prestamo
=============================================================
 Conceptos POO demostrados:
   - Composición (◆): Prestamo contiene Libro y Socio
   - Atributos de clase: DIAS_PRESTAMO, DIAS_PRESTAMO_VIP
   - Propiedades calculadas: esta_activo, esta_vencido
   - Polimorfismo: el plazo varía según el tipo de socio
   - Métodos especiales: __str__
=============================================================
"""

from __future__ import annotations

from datetime import date, timedelta
from typing import TYPE_CHECKING, Optional

from models.libro import Libro

# Importación diferida solo para type hints (evita importación circular)
if TYPE_CHECKING:
    from models.socio import Socio, SocioVIP


class Prestamo:
    """
    Registra el préstamo de un libro a un socio.

    Relación de COMPOSICIÓN con Libro y Socio:
    el préstamo no tiene sentido sin ambos objetos.

    Atributos de clase (compartidos por todas las instancias):
        DIAS_PRESTAMO     (int): plazo estándar en días (14).
        DIAS_PRESTAMO_VIP (int): plazo VIP en días (21).
    """

    # ── Atributos de clase (→ subrayados en UML) ────────────────────
    DIAS_PRESTAMO:     int = 14
    DIAS_PRESTAMO_VIP: int = 21

    def __init__(self, libro: Libro, socio: "Socio") -> None:
        """
        Crea el préstamo y marca el libro como no disponible.

        Args:
            libro: objeto Libro a prestar.
            socio: objeto Socio o SocioVIP que lo solicita.

        Raises:
            ValueError: si el libro ya está prestado (lo lanza Libro).
        """
        # Importación local para evitar circularidad en tiempo de ejecución
        from models.socio import SocioVIP

        self._libro = libro
        self._socio = socio
        self.fecha_inicio: date = date.today()

        # El plazo varía según si el socio es VIP → polimorfismo implícito
        dias = (
            self.DIAS_PRESTAMO_VIP
            if isinstance(socio, SocioVIP)
            else self.DIAS_PRESTAMO
        )
        self.fecha_venc: date                = self.fecha_inicio + timedelta(days=dias)
        self.fecha_dev:  Optional[date]      = None   # None = aún no devuelto

        # Efecto secundario: el libro pasa a no disponible
        libro.marcar_prestado()

    # ── Propiedades calculadas ──────────────────────────────────────
    @property
    def esta_activo(self) -> bool:
        """True si el préstamo aún no fue devuelto."""
        return self.fecha_dev is None

    @property
    def esta_vencido(self) -> bool:
        """True si está activo Y la fecha de vencimiento ya pasó."""
        return self.esta_activo and date.today() > self.fecha_venc

    # ── Operación de devolución ─────────────────────────────────────
    def devolver(self) -> None:
        """
        Registra la devolución del libro.

        Raises:
            ValueError: si el préstamo ya fue devuelto anteriormente.
        """
        if not self.esta_activo:
            raise ValueError("Este préstamo ya fue devuelto.")
        self.fecha_dev = date.today()
        self._libro.marcar_devuelto()

    # ── Métodos especiales ──────────────────────────────────────────
    def __str__(self) -> str:
        estado = "ACTIVO" if self.esta_activo else "DEVUELTO"
        alerta = "  ⚠️  VENCIDO" if self.esta_vencido else ""
        return (
            f"Préstamo [{estado}{alerta}]\n"
            f"  Libro  : {self._libro.titulo}\n"
            f"  Socio  : {self._socio.nombre}\n"
            f"  Inicio : {self.fecha_inicio}  |  Vence: {self.fecha_venc}"
        )

    def __repr__(self) -> str:
        return (
            f"Prestamo(libro={self._libro.titulo!r}, "
            f"socio={self._socio.nombre!r}, "
            f"activo={self.esta_activo})"
        )
