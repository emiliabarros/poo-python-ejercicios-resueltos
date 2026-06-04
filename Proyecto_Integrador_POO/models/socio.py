"""
=============================================================
 MODELOS: Socio, SocioVIP, Bibliotecario
=============================================================
 Conceptos POO demostrados:
   - Herencia simple:    Socio → Persona
   - Herencia simple:    SocioVIP → Socio
   - Herencia simple:    Bibliotecario → Persona
   - Polimorfismo:       presentarse() diferente en cada clase
   - Atributo de clase:  MAX_PRESTAMOS sobreescrito en SocioVIP
   - Agregación (◇):     Socio agrega objetos Prestamo
   - Métodos especiales: __len__
=============================================================
"""

from __future__ import annotations

from typing import List

from models.persona import Persona


# ═══════════════════════════════════════════════════════════════════
#  SOCIO
# ═══════════════════════════════════════════════════════════════════
class Socio(Persona):
    """
    Representa a un socio regular de la biblioteca.

    Hereda de Persona e implementa presentarse().
    Agrega (◇) objetos Prestamo: los préstamos se crean
    fuera del socio y se añaden mediante agregar_prestamo().

    Atributo de clase:
        MAX_PRESTAMOS (int): cantidad máxima de préstamos simultáneos.
    """

    # Atributo de CLASE: compartido, sobreescribible en subclases
    MAX_PRESTAMOS: int = 3

    def __init__(self, nombre: str, dni: str, nro_socio: str) -> None:
        super().__init__(nombre, dni)           # inicializa la parte Persona
        self.nro_socio = nro_socio
        # Agregación ◇: los préstamos existen independientemente del socio
        self._prestamos: List = []

    # ── Implementación del contrato abstracto ───────────────────────
    def presentarse(self) -> str:
        return f"Soy {self.nombre}, socio N° {self.nro_socio}"

    # ── Propiedades calculadas ──────────────────────────────────────
    @property
    def prestamos_activos(self) -> List:
        """Lista de préstamos que aún no fueron devueltos."""
        return [p for p in self._prestamos if p.esta_activo]

    # ── Gestión de préstamos ────────────────────────────────────────
    def puede_pedir_prestamo(self) -> bool:
        """True si el socio no alcanzó su límite de préstamos simultáneos."""
        return len(self.prestamos_activos) < self.MAX_PRESTAMOS

    def agregar_prestamo(self, prestamo) -> None:
        """Agrega un préstamo al historial del socio."""
        self._prestamos.append(prestamo)

    def historial(self) -> str:
        """Devuelve el historial completo de préstamos como texto."""
        if not self._prestamos:
            return f"{self.nombre} no tiene préstamos registrados."
        return "\n".join(str(p) for p in self._prestamos)

    # ── Métodos especiales ──────────────────────────────────────────
    def __len__(self) -> int:
        """len(socio) → cantidad de préstamos ACTIVOS en este momento."""
        return len(self.prestamos_activos)

    def __str__(self) -> str:
        activos = len(self.prestamos_activos)
        return (
            f"{super().__str__()} | Socio N° {self.nro_socio} "
            f"| Préstamos activos: {activos}/{self.MAX_PRESTAMOS}"
        )


# ═══════════════════════════════════════════════════════════════════
#  SOCIO VIP
# ═══════════════════════════════════════════════════════════════════
class SocioVIP(Socio):
    """
    Socio con privilegios extendidos.

    Hereda TODO de Socio y solo sobreescribe:
      - MAX_PRESTAMOS: puede llevar más libros a la vez (7 vs 3).
      - presentarse(): agrega la etiqueta VIP.

    El plazo de préstamo también es mayor (21 días vs 14),
    pero esa lógica vive en Prestamo, no aquí.
    """

    # Sobreescribe el atributo de clase del padre
    MAX_PRESTAMOS: int = 7

    def presentarse(self) -> str:
        return f"Soy {self.nombre}, socio VIP N° {self.nro_socio} ⭐"


# ═══════════════════════════════════════════════════════════════════
#  BIBLIOTECARIO
# ═══════════════════════════════════════════════════════════════════
class Bibliotecario(Persona):
    """
    Representa al personal bibliotecario del sistema.

    Hereda de Persona (NO de Socio: el bibliotecario no pide préstamos).
    Implementa presentarse() con su legajo laboral.
    """

    def __init__(self, nombre: str, dni: str, legajo: str) -> None:
        super().__init__(nombre, dni)
        self.legajo = legajo

    def presentarse(self) -> str:
        return f"Soy {self.nombre}, bibliotecario (legajo: {self.legajo})"

    def __str__(self) -> str:
        return f"{super().__str__()} | Legajo: {self.legajo}"
