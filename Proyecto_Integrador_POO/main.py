"""
=============================================================
 SISTEMA DE GESTIÓN DE BIBLIOTECA
 Proyecto Integrador — Programación Orientada a Objetos en Python

 Paso 4: Demo de funcionamiento
=============================================================
 Ejecutar desde la raíz del proyecto:
     python main.py
=============================================================
 Conceptos POO demostrados en este archivo:
   ✅ Instanciación de objetos
   ✅ Polimorfismo: presentarse() en Socio y SocioVIP
   ✅ Agregación: libros/socios creados fuera de Biblioteca
   ✅ Composición: Prestamo creado dentro de Biblioteca
   ✅ Encapsulamiento: acceso a saldo a través de métodos
   ✅ Herencia: Socio → SocioVIP
   ✅ Manejo de excepciones con try/except
=============================================================
"""

from models          import Libro, Socio, SocioVIP, Bibliotecario
from services        import Biblioteca
from utils.datos_demo import crear_libros, crear_socios


def separador(titulo: str = "") -> None:
    """Imprime una línea separadora con título opcional."""
    print(f"\n── {titulo} {'─' * (42 - len(titulo))}" if titulo else f"\n{'─' * 50}")


def main() -> None:
    print("\n🏛️  INICIANDO SISTEMA DE GESTIÓN DE BIBLIOTECA\n")

    # ══════════════════════════════════════════════════════════════
    #  1. CREAR LA BIBLIOTECA
    # ══════════════════════════════════════════════════════════════
    bib = Biblioteca("Biblioteca Central")
    print(bib)   # __str__ → Biblioteca «Biblioteca Central» — 0 libros

    # ══════════════════════════════════════════════════════════════
    #  2. CARGAR CATÁLOGO  — Agregación ◇
    #     Los libros existen FUERA de la biblioteca.
    #     Si la biblioteca desapareciera, los libros seguirían existiendo.
    # ══════════════════════════════════════════════════════════════
    separador("Cargando catálogo")

    l1 = Libro("978-0-06-112008-4", "Cien años de soledad", "García Márquez",   1967)
    l2 = Libro("978-0-14-028329-7", "El Principito",         "Saint-Exupéry",   1943)
    l3 = Libro("978-84-376-0494-7", "La Odisea",             "Homero",          -800)
    l4 = Libro("978-0-7432-7356-5", "Clean Code",            "Robert C. Martin", 2008)

    for libro in [l1, l2, l3, l4]:
        bib.agregar_libro(libro)

    bib.listar_libros()

    # ══════════════════════════════════════════════════════════════
    #  3. REGISTRAR SOCIOS  — Agregación ◇
    # ══════════════════════════════════════════════════════════════
    separador("Registrando socios")

    ana    = Socio("Ana López",       "12345678", "S001")
    carlos = SocioVIP("Carlos Gómez", "87654321", "S002")
    bib.registrar_socio(ana)
    bib.registrar_socio(carlos)

    bib.listar_socios()

    # ══════════════════════════════════════════════════════════════
    #  4. POLIMORFISMO — presentarse()
    #     Mismo mensaje, respuesta diferente según el tipo de objeto.
    # ══════════════════════════════════════════════════════════════
    separador("Polimorfismo: presentarse()")

    for persona in [ana, carlos]:
        print(f"  → {persona.presentarse()}")

    # ══════════════════════════════════════════════════════════════
    #  5. REALIZAR PRÉSTAMOS  — Composición ◆
    #     Prestamo se crea DENTRO de prestar_libro().
    #     Si el préstamo desapareciera, el libro y el socio siguen existiendo.
    # ══════════════════════════════════════════════════════════════
    separador("Realizando préstamos")

    p1 = bib.prestar_libro("978-0-06-112008-4", "S001")  # Ana  ← Cien años
    p2 = bib.prestar_libro("978-0-14-028329-7", "S002")  # Carlos ← El Principito
    p3 = bib.prestar_libro("978-84-376-0494-7", "S001")  # Ana  ← La Odisea

    print(f"\n  Estado de Ana después de 2 préstamos:")
    print(f"  {ana}")                                      # __str__ con conteo
    print(f"\n  Plazo de Carlos (VIP, {p2.fecha_venc}):")
    print(f"  Plazo de Ana    (regular, {p1.fecha_venc})")
    print(f"  → Carlos tiene {(p2.fecha_venc - p1.fecha_venc).days} días extra.")

    # ══════════════════════════════════════════════════════════════
    #  6. REPORTE DE ESTADO
    # ══════════════════════════════════════════════════════════════
    print(bib.reporte())

    # ══════════════════════════════════════════════════════════════
    #  7. DEVOLUCIÓN
    # ══════════════════════════════════════════════════════════════
    separador("Devolviendo libro")

    bib.devolver_libro("978-0-06-112008-4", "S001")
    print(f"  {l1}")   # [DISPONIBLE] «Cien años de soledad» — ...

    # ══════════════════════════════════════════════════════════════
    #  8. HISTORIAL DEL SOCIO
    # ══════════════════════════════════════════════════════════════
    separador(f"Historial de {ana.nombre}")
    print(ana.historial())

    # ══════════════════════════════════════════════════════════════
    #  9. TEST DE ERRORES ESPERADOS
    # ══════════════════════════════════════════════════════════════
    separador("Test: límite de préstamos y errores")

    # Ana ya tiene 1 activo (La Odisea). Puede pedir hasta 3.
    try:
        bib.prestar_libro("978-0-7432-7356-5", "S001")  # Ana pide Clean Code → 2 activos
        print("  ✅ Clean Code prestado a Ana (2/3 activos)")
    except ValueError as e:
        print(f"  ❌ Error inesperado: {e}")

    try:
        # Ana ya tiene 2 activos + el límite es 3.
        # Intentamos prestar Cien años (ahora disponible) → 3 activos → OK
        bib.prestar_libro("978-0-06-112008-4", "S001")
        print("  ✅ Cien años prestado a Ana (3/3 activos)")
    except ValueError as e:
        print(f"  ❌ Error inesperado: {e}")

    try:
        # Ana ya tiene 3 activos → debe fallar
        bib.prestar_libro("978-0-14-028329-7", "S001")
        print("  ❌ No debería llegar aquí.")
    except ValueError as e:
        print(f"  ✅ Error esperado (límite alcanzado): {e}")

    try:
        # ISBN inexistente
        bib.prestar_libro("ISBN-FALSO", "S001")
    except ValueError as e:
        print(f"  ✅ Error esperado (ISBN no existe): {e}")

    try:
        # Devolver algo que no fue prestado
        bib.devolver_libro("978-0-14-028329-7", "S001")
    except ValueError as e:
        print(f"  ✅ Error esperado (sin préstamo activo): {e}")

    # ══════════════════════════════════════════════════════════════
    #  10. REPORTE FINAL
    # ══════════════════════════════════════════════════════════════
    print(bib.reporte())
    print("\n✅ Sistema de Biblioteca funcionando correctamente.\n")


if __name__ == "__main__":
    main()
