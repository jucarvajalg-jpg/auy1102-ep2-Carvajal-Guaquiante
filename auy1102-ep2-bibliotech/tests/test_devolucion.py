"""Pruebas de calcular_fecha_devolucion() (Parte 2C, TDD).

Estas dos pruebas son el punto de partida. Escriban las demás ANTES
de implementar la función en bibliotech/prestamos.py.
"""
from datetime import date

from bibliotech.prestamos import calcular_fecha_devolucion


def test_estudiante_devuelve_en_7_dias():
    # lunes 5 de octubre de 2026 + 7 días = lunes 12 de octubre
    assert calcular_fecha_devolucion(date(2026, 10, 5), "estudiante") == date(2026, 10, 12)


def test_docente_devuelve_en_14_dias():
    # lunes 5 de octubre de 2026 + 14 días = lunes 19 de octubre
    assert calcular_fecha_devolucion(date(2026, 10, 5), "docente") == date(2026, 10, 19)


# ---------- PARTE 2C: escriban sus pruebas aquí ----------
