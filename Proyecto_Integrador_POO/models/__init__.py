"""
Paquete models — clases de dominio del Sistema de Biblioteca.

Importaciones disponibles:
    from models import Persona, Libro, Prestamo, Socio, SocioVIP, Bibliotecario
"""

from models.persona       import Persona
from models.libro         import Libro
from models.prestamo      import Prestamo
from models.socio         import Socio, SocioVIP, Bibliotecario

__all__ = [
    "Persona",
    "Libro",
    "Prestamo",
    "Socio",
    "SocioVIP",
    "Bibliotecario",
]
