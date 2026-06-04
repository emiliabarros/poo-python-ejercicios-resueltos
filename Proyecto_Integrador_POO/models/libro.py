"""
=============================================================
 MODELO: Libro
=============================================================
 Conceptos POO demostrados:
   - Encapsulamiento: _disponible con @property
   - Métodos especiales: __str__, __eq__
   - Validación de estado (no se puede prestar si ya está prestado)
=============================================================
"""


class Libro:
    """
    Representa un libro del catálogo de la biblioteca.

    Atributos públicos:
        isbn   (str): identificador único internacional.
        titulo (str): título del libro.
        autor  (str): nombre del autor.
        anio   (int): año de publicación.

    Atributo protegido:
        _disponible (bool): True si el libro no está prestado.
    """

    def __init__(self, isbn: str, titulo: str, autor: str, anio: int) -> None:
        self.isbn   = isbn
        self.titulo = titulo
        self.autor  = autor
        self.anio   = anio
        # Atributo protegido: se gestiona solo a través de los métodos
        # marcar_prestado() y marcar_devuelto()
        self._disponible: bool = True

    # ── Propiedad de solo lectura ───────────────────────────────────
    @property
    def disponible(self) -> bool:
        """Indica si el libro se puede prestar en este momento."""
        return self._disponible

    # ── Gestión de estado ───────────────────────────────────────────
    def marcar_prestado(self) -> None:
        """
        Marca el libro como prestado.

        Raises:
            ValueError: si el libro ya está prestado.
        """
        if not self._disponible:
            raise ValueError(f"«{self.titulo}» ya está prestado.")
        self._disponible = False

    def marcar_devuelto(self) -> None:
        """Marca el libro como disponible nuevamente."""
        self._disponible = True

    # ── Métodos especiales ──────────────────────────────────────────
    def __str__(self) -> str:
        estado = "DISPONIBLE" if self._disponible else "PRESTADO"
        return f"[{estado}] «{self.titulo}» — {self.autor} ({self.anio})"

    def __repr__(self) -> str:
        return (
            f"Libro(isbn={self.isbn!r}, titulo={self.titulo!r}, "
            f"autor={self.autor!r}, anio={self.anio!r})"
        )

    def __eq__(self, otro: object) -> bool:
        """Dos libros son iguales si tienen el mismo ISBN."""
        return isinstance(otro, Libro) and self.isbn == otro.isbn
