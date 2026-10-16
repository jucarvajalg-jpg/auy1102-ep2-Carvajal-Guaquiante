"""Pruebas de calcular_multa() (Parte 2B).

Todas pasan, pero la función no cumple completamente el REQUISITO
escrito en bibliotech/prestamos.py. Agreguen sus pruebas al final.
"""
import pytest  # noqa: F401  (lo necesitarán para pytest.raises)

from bibliotech.prestamos import calcular_multa


def test_estudiante_con_3_dias_de_atraso_paga_1500():
    assert calcular_multa(3, "estudiante") == 1500


def test_multa_alta_queda_en_el_tope():
    assert calcular_multa(30, "estudiante") == 10000


def test_docente_con_5_dias_paga_solo_3():
    assert calcular_multa(5, "docente") == 1500


# ---------- PARTE 2B: escriban sus pruebas aquí ----------
