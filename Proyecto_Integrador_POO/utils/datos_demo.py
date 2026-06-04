"""
=============================================================
 UTILIDAD: datos_demo.py
 Datos de ejemplo para la demo y los tests.
=============================================================
 Uso:
     from utils.datos_demo import crear_libros, crear_socios
=============================================================
"""

from models.libro  import Libro
from models.socio  import Socio, SocioVIP, Bibliotecario


def crear_libros() -> list[Libro]:
    """Devuelve una lista de libros de ejemplo."""
    return [
        Libro("978-0-06-112008-4", "Cien años de soledad", "García Márquez",  1967),
        Libro("978-0-14-028329-7", "El Principito",         "Saint-Exupéry",  1943),
        Libro("978-84-376-0494-7", "La Odisea",             "Homero",         -800),
        Libro("978-0-7432-7356-5", "Clean Code",            "Robert C. Martin", 2008),
    ]


def crear_socios() -> list:
    """Devuelve una lista con socios de ejemplo (regular y VIP)."""
    return [
        Socio("Ana López",    "12345678", "S001"),
        SocioVIP("Carlos Gómez", "87654321", "S002"),
    ]


def crear_bibliotecario() -> Bibliotecario:
    """Devuelve un bibliotecario de ejemplo."""
    return Bibliotecario("María Fernández", "55667788", "BIB-001")
