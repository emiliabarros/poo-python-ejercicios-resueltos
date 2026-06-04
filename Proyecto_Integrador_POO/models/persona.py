"""
=============================================================
 MODELO: Persona
 Clase abstracta base para todas las personas del sistema.
=============================================================
 Conceptos POO demostrados:
   - Clase abstracta (ABC)
   - Encapsulamiento: atributos privados con @property
   - Métodos especiales: __str__, __repr__
   - @abstractmethod: contrato para las subclases
=============================================================
"""

from abc import ABC, abstractmethod


class Persona(ABC):
    """
    Clase abstracta que representa a cualquier persona del sistema.

    No puede instanciarse directamente. Las subclases concretas
    (Socio, SocioVIP, Bibliotecario) deben implementar presentarse().

    Atributos privados (name mangling):
        __nombre (str): nombre completo de la persona.
        __dni    (str): documento nacional de identidad.
    """

    def __init__(self, nombre: str, dni: str) -> None:
        # Atributos privados → símbolo "-" en UML
        # Python aplica name mangling: __nombre → _Persona__nombre
        self.__nombre = nombre
        self.__dni    = dni

    # ── Propiedades de solo lectura ─────────────────────────────────
    @property
    def nombre(self) -> str:
        """Devuelve el nombre de la persona (solo lectura)."""
        return self.__nombre

    @property
    def dni(self) -> str:
        """Devuelve el DNI de la persona (solo lectura)."""
        return self.__dni

    # ── Método abstracto ────────────────────────────────────────────
    @abstractmethod
    def presentarse(self) -> str:
        """
        Cada subclase concreta define cómo se presenta.

        Returns:
            str: mensaje de presentación personalizado.
        """
        pass

    # ── Métodos especiales ──────────────────────────────────────────
    def __str__(self) -> str:
        """Representación amigable para el usuario final."""
        return f"{self.nombre} (DNI: {self.dni})"

    def __repr__(self) -> str:
        """Representación técnica: cómo recrear el objeto."""
        return f"{type(self).__name__}({self.nombre!r}, {self.dni!r})"
