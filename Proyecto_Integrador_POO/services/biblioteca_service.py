"""
=============================================================
 SERVICIO: Biblioteca
=============================================================
 Conceptos POO demostrados:
   - Agregación (◇): agrega Libro y Socio (existen fuera)
   - Composición (◆): crea Prestamo internamente
   - Encapsulamiento: métodos de búsqueda privados (_buscar_*)
   - Métodos especiales: __len__, __str__
   - Separación de responsabilidades (SRP):
       • gestión del catálogo
       • gestión de socios
       • operaciones de préstamo
       • generación de reportes
=============================================================
"""

from typing import List

from models.libro    import Libro
from models.prestamo import Prestamo
from models.socio    import Socio


class Biblioteca:
    """
    Clase principal del sistema. Orquesta libros, socios y préstamos.

    Relaciones:
        ◇ agrega Libro  : los libros existen fuera de la biblioteca.
        ◇ agrega Socio  : los socios existen fuera de la biblioteca.
        ◆ crea Prestamo : el préstamo se instancia aquí y no tiene
                          sentido sin la biblioteca que lo gestiona.
    """

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        # Agregación ◇ — objetos creados FUERA y pasados como argumento
        self._libros:    List[Libro]    = []
        self._socios:    List[Socio]    = []
        # Composición ◆ — objetos Prestamo creados DENTRO en prestar_libro()
        self._prestamos: List[Prestamo] = []

    # ══════════════════════════════════════════════════════════════
    #  GESTIÓN DEL CATÁLOGO
    # ══════════════════════════════════════════════════════════════

    def agregar_libro(self, libro: Libro) -> None:
        """Incorpora un libro al catálogo."""
        self._libros.append(libro)
        print(f"  ✅ Libro agregado: {libro.titulo}")

    def registrar_socio(self, socio: Socio) -> None:
        """Registra un socio en el sistema."""
        self._socios.append(socio)
        print(f"  ✅ Socio registrado: {socio.nombre}")

    # ══════════════════════════════════════════════════════════════
    #  OPERACIONES DE PRÉSTAMO
    # ══════════════════════════════════════════════════════════════

    def prestar_libro(self, isbn: str, nro_socio: str) -> Prestamo:
        """
        Crea un préstamo entre un libro y un socio.

        Args:
            isbn      (str): ISBN del libro a prestar.
            nro_socio (str): número de socio que lo solicita.

        Returns:
            Prestamo: el objeto préstamo recién creado.

        Raises:
            ValueError: si el libro no está disponible.
            ValueError: si el socio alcanzó su límite de préstamos.
            ValueError: si el ISBN o número de socio no existen.
        """
        libro = self._buscar_libro(isbn)
        socio = self._buscar_socio(nro_socio)

        if not libro.disponible:
            raise ValueError(f"«{libro.titulo}» no está disponible.")
        if not socio.puede_pedir_prestamo():
            raise ValueError(
                f"{socio.nombre} alcanzó el límite de "
                f"{socio.MAX_PRESTAMOS} préstamos simultáneos."
            )

        # Composición ◆: Prestamo nace aquí
        prestamo = Prestamo(libro, socio)
        socio.agregar_prestamo(prestamo)
        self._prestamos.append(prestamo)

        print(f"  📚 Préstamo registrado: «{libro.titulo}» → {socio.nombre}")
        return prestamo

    def devolver_libro(self, isbn: str, nro_socio: str) -> Prestamo:
        """
        Registra la devolución de un libro.

        Args:
            isbn      (str): ISBN del libro que se devuelve.
            nro_socio (str): número del socio que lo devuelve.

        Returns:
            Prestamo: el préstamo que fue cerrado.

        Raises:
            ValueError: si no existe un préstamo activo para ese par.
        """
        for prestamo in self._prestamos:
            if (
                prestamo.esta_activo
                and prestamo._libro.isbn    == isbn
                and prestamo._socio.nro_socio == nro_socio
            ):
                prestamo.devolver()
                print(f"  🔄 Devolución registrada: «{prestamo._libro.titulo}»")
                return prestamo

        raise ValueError(
            f"No existe un préstamo activo del ISBN {isbn} "
            f"para el socio {nro_socio}."
        )

    # ══════════════════════════════════════════════════════════════
    #  REPORTES
    # ══════════════════════════════════════════════════════════════

    def reporte(self) -> str:
        """Genera un reporte del estado actual de la biblioteca."""
        activos  = [p for p in self._prestamos if p.esta_activo]
        vencidos = [p for p in activos if p.esta_vencido]

        sep = "=" * 50
        lineas = [
            f"\n{sep}",
            f"  REPORTE: {self.nombre}",
            sep,
            f"  Libros en catálogo : {len(self._libros)}",
            f"  Socios registrados : {len(self._socios)}",
            f"  Préstamos activos  : {len(activos)}",
            f"  Préstamos vencidos : {len(vencidos)}",
            sep,
        ]

        if activos:
            lineas.append("  Préstamos activos:")
            for p in activos:
                alerta = "  ⚠️" if p.esta_vencido else ""
                lineas.append(f"    • {p._libro.titulo} → {p._socio.nombre}{alerta}")

        return "\n".join(lineas)

    def listar_libros(self) -> None:
        """Imprime el catálogo completo con estado de disponibilidad."""
        print(f"\n  {'─'*44}")
        print(f"  CATÁLOGO — {self.nombre}")
        print(f"  {'─'*44}")
        if not self._libros:
            print("  (sin libros cargados)")
        for libro in self._libros:
            print(f"  {libro}")

    def listar_socios(self) -> None:
        """Imprime la lista de socios registrados."""
        print(f"\n  {'─'*44}")
        print(f"  SOCIOS — {self.nombre}")
        print(f"  {'─'*44}")
        if not self._socios:
            print("  (sin socios registrados)")
        for socio in self._socios:
            print(f"  {socio}")

    # ══════════════════════════════════════════════════════════════
    #  BÚSQUEDAS INTERNAS (privadas)
    # ══════════════════════════════════════════════════════════════

    def _buscar_libro(self, isbn: str) -> Libro:
        """Busca un libro por ISBN. Lanza ValueError si no existe."""
        for libro in self._libros:
            if libro.isbn == isbn:
                return libro
        raise ValueError(f"Libro con ISBN «{isbn}» no encontrado.")

    def _buscar_socio(self, nro: str) -> Socio:
        """Busca un socio por número. Lanza ValueError si no existe."""
        for socio in self._socios:
            if socio.nro_socio == nro:
                return socio
        raise ValueError(f"Socio N° «{nro}» no encontrado.")

    # ══════════════════════════════════════════════════════════════
    #  MÉTODOS ESPECIALES
    # ══════════════════════════════════════════════════════════════

    def __len__(self) -> int:
        """len(biblioteca) → cantidad de libros en el catálogo."""
        return len(self._libros)

    def __str__(self) -> str:
        return f"Biblioteca «{self.nombre}» — {len(self)} libros"

    def __repr__(self) -> str:
        return f"Biblioteca(nombre={self.nombre!r}, libros={len(self)})"
