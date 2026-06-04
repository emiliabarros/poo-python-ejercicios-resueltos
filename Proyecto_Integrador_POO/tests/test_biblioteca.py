"""
=============================================================
 TESTS: test_biblioteca.py
 Pruebas unitarias del Sistema de Biblioteca.
=============================================================
 Ejecutar desde la raíz del proyecto:
     python -m pytest tests/ -v
   o bien:
     python tests/test_biblioteca.py
=============================================================
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from datetime import date

from models.libro    import Libro
from models.socio    import Socio, SocioVIP, Bibliotecario
from models.prestamo import Prestamo
from services        import Biblioteca


# ══════════════════════════════════════════════════════════════════
#  TESTS — LIBRO
# ══════════════════════════════════════════════════════════════════
class TestLibro(unittest.TestCase):

    def setUp(self):
        self.libro = Libro("ISBN-001", "Python POO", "Autor Test", 2024)

    def test_disponible_al_crear(self):
        self.assertTrue(self.libro.disponible)

    def test_marcar_prestado(self):
        self.libro.marcar_prestado()
        self.assertFalse(self.libro.disponible)

    def test_prestar_dos_veces_lanza_error(self):
        self.libro.marcar_prestado()
        with self.assertRaises(ValueError):
            self.libro.marcar_prestado()

    def test_marcar_devuelto(self):
        self.libro.marcar_prestado()
        self.libro.marcar_devuelto()
        self.assertTrue(self.libro.disponible)

    def test_igualdad_por_isbn(self):
        otro = Libro("ISBN-001", "Otro título", "Otro autor", 2000)
        self.assertEqual(self.libro, otro)

    def test_desigualdad_isbn_diferente(self):
        otro = Libro("ISBN-999", "Python POO", "Autor Test", 2024)
        self.assertNotEqual(self.libro, otro)

    def test_str_disponible(self):
        self.assertIn("DISPONIBLE", str(self.libro))

    def test_str_prestado(self):
        self.libro.marcar_prestado()
        self.assertIn("PRESTADO", str(self.libro))


# ══════════════════════════════════════════════════════════════════
#  TESTS — SOCIO
# ══════════════════════════════════════════════════════════════════
class TestSocio(unittest.TestCase):

    def setUp(self):
        self.socio = Socio("Ana", "12345678", "S001")

    def test_max_prestamos_regular(self):
        self.assertEqual(Socio.MAX_PRESTAMOS, 3)

    def test_max_prestamos_vip(self):
        self.assertEqual(SocioVIP.MAX_PRESTAMOS, 7)

    def test_puede_pedir_prestamo_inicial(self):
        self.assertTrue(self.socio.puede_pedir_prestamo())

    def test_len_inicial_cero(self):
        self.assertEqual(len(self.socio), 0)

    def test_presentarse_regular(self):
        self.assertIn("S001", self.socio.presentarse())
        self.assertNotIn("VIP", self.socio.presentarse())

    def test_presentarse_vip(self):
        vip = SocioVIP("Carlos", "87654321", "S002")
        self.assertIn("VIP", vip.presentarse())
        self.assertIn("⭐", vip.presentarse())

    def test_historial_sin_prestamos(self):
        self.assertIn("no tiene", self.socio.historial())

    def test_bibliotecario_presentarse(self):
        bib = Bibliotecario("María", "55667788", "BIB-001")
        self.assertIn("bibliotecario", bib.presentarse())
        self.assertIn("BIB-001", bib.presentarse())


# ══════════════════════════════════════════════════════════════════
#  TESTS — BIBLIOTECA (integración)
# ══════════════════════════════════════════════════════════════════
class TestBiblioteca(unittest.TestCase):

    def setUp(self):
        self.bib   = Biblioteca("Biblioteca Test")
        self.l1    = Libro("ISBN-001", "Libro Uno",  "Autor A", 2020)
        self.l2    = Libro("ISBN-002", "Libro Dos",  "Autor B", 2021)
        self.l3    = Libro("ISBN-003", "Libro Tres", "Autor C", 2022)
        self.l4    = Libro("ISBN-004", "Libro Cuatro","Autor D", 2023)
        self.ana   = Socio("Ana",   "12345678", "S001")
        self.carlos = SocioVIP("Carlos", "87654321", "S002")

        for libro in [self.l1, self.l2, self.l3, self.l4]:
            self.bib.agregar_libro(libro)
        self.bib.registrar_socio(self.ana)
        self.bib.registrar_socio(self.carlos)

    # ── len y str ──────────────────────────────────────────────────
    def test_len_biblioteca(self):
        self.assertEqual(len(self.bib), 4)

    def test_str_contiene_nombre(self):
        self.assertIn("Biblioteca Test", str(self.bib))

    # ── préstamos básicos ──────────────────────────────────────────
    def test_prestar_libro_disponible(self):
        prestamo = self.bib.prestar_libro("ISBN-001", "S001")
        self.assertIsNotNone(prestamo)
        self.assertTrue(prestamo.esta_activo)
        self.assertFalse(self.l1.disponible)

    def test_devolver_libro(self):
        self.bib.prestar_libro("ISBN-001", "S001")
        self.bib.devolver_libro("ISBN-001", "S001")
        self.assertTrue(self.l1.disponible)

    # ── errores esperados ──────────────────────────────────────────
    def test_prestar_libro_no_disponible_lanza_error(self):
        self.bib.prestar_libro("ISBN-001", "S001")
        with self.assertRaises(ValueError):
            self.bib.prestar_libro("ISBN-001", "S002")

    def test_isbn_inexistente_lanza_error(self):
        with self.assertRaises(ValueError):
            self.bib.prestar_libro("ISBN-999", "S001")

    def test_socio_inexistente_lanza_error(self):
        with self.assertRaises(ValueError):
            self.bib.prestar_libro("ISBN-001", "S999")

    def test_devolver_sin_prestamo_activo_lanza_error(self):
        with self.assertRaises(ValueError):
            self.bib.devolver_libro("ISBN-001", "S001")

    # ── límite de préstamos ────────────────────────────────────────
    def test_limite_prestamos_regular(self):
        """Un socio regular no puede tener más de 3 préstamos activos."""
        self.bib.prestar_libro("ISBN-001", "S001")
        self.bib.prestar_libro("ISBN-002", "S001")
        self.bib.prestar_libro("ISBN-003", "S001")
        with self.assertRaises(ValueError):
            self.bib.prestar_libro("ISBN-004", "S001")

    def test_limite_prestamos_vip_mayor(self):
        """Un socio VIP puede pedir más préstamos que uno regular."""
        self.assertEqual(SocioVIP.MAX_PRESTAMOS, 7)
        self.assertGreater(SocioVIP.MAX_PRESTAMOS, Socio.MAX_PRESTAMOS)

    # ── plazo diferenciado ─────────────────────────────────────────
    def test_plazo_vip_mayor_que_regular(self):
        p_regular = self.bib.prestar_libro("ISBN-001", "S001")
        p_vip     = self.bib.prestar_libro("ISBN-002", "S002")
        self.assertGreater(p_vip.fecha_venc, p_regular.fecha_venc)

    # ── reporte ────────────────────────────────────────────────────
    def test_reporte_contiene_nombre_biblioteca(self):
        reporte = self.bib.reporte()
        self.assertIn("Biblioteca Test", reporte)

    def test_reporte_refleja_prestamos_activos(self):
        self.bib.prestar_libro("ISBN-001", "S001")
        reporte = self.bib.reporte()
        self.assertIn("Libro Uno", reporte)


# ══════════════════════════════════════════════════════════════════
#  TESTS — PRESTAMO
# ══════════════════════════════════════════════════════════════════
class TestPrestamo(unittest.TestCase):

    def setUp(self):
        self.libro = Libro("ISBN-001", "Test", "Autor", 2024)
        self.socio = Socio("Ana", "12345678", "S001")
        self.prestamo = Prestamo(self.libro, self.socio)

    def test_activo_al_crear(self):
        self.assertTrue(self.prestamo.esta_activo)

    def test_no_vencido_al_crear(self):
        # Un préstamo recién creado no debería estar vencido
        self.assertFalse(self.prestamo.esta_vencido)

    def test_fecha_venc_regular(self):
        esperada = date.today().__class__.today()
        from datetime import timedelta
        esperada = date.today() + timedelta(days=Prestamo.DIAS_PRESTAMO)
        self.assertEqual(self.prestamo.fecha_venc, esperada)

    def test_plazo_vip(self):
        from datetime import timedelta
        libro_vip  = Libro("ISBN-VIP", "VIP Test", "Autor", 2024)
        socio_vip  = SocioVIP("Carlos", "87654321", "S002")
        p_vip      = Prestamo(libro_vip, socio_vip)
        esperada   = date.today() + timedelta(days=Prestamo.DIAS_PRESTAMO_VIP)
        self.assertEqual(p_vip.fecha_venc, esperada)

    def test_devolver(self):
        self.prestamo.devolver()
        self.assertFalse(self.prestamo.esta_activo)
        self.assertIsNotNone(self.prestamo.fecha_dev)
        self.assertTrue(self.libro.disponible)

    def test_devolver_dos_veces_lanza_error(self):
        self.prestamo.devolver()
        with self.assertRaises(ValueError):
            self.prestamo.devolver()


# ══════════════════════════════════════════════════════════════════
#  PUNTO DE ENTRADA
# ══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    unittest.main(verbosity=2)
