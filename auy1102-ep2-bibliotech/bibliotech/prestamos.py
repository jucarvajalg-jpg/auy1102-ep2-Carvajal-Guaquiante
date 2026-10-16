"""Reglas de préstamo de BiblioTech."""
import os
from datetime import date, timedelta

VALOR_DIA_ATRASO = 500
MULTA_MAXIMA = 10000
DIAS_GRACIA_DOCENTE = 2


def calcular_multa(dias_atraso, tipo_usuario):
    """Calcula la multa en pesos por devolver un libro con atraso.

    REQUISITO (acordado con la jefatura de la biblioteca):
      - Cada día de atraso cuesta $500.
      - La multa nunca supera los $10.000.
      - Los usuarios "docente" tienen 2 días de gracia: sus primeros 2 días
        de atraso no se cobran.
      - Si no hay atraso (0 días), la multa es $0.
      - Una cantidad de días negativa no tiene sentido: debe lanzar ValueError.
    """
    dias_cobrables = dias_atraso
    if tipo_usuario == "docente":
        dias_cobrables = dias_atraso - DIAS_GRACIA_DOCENTE
    multa = dias_cobrables*VALOR_DIA_ATRASO
    if multa > MULTA_MAXIMA:
        multa = MULTA_MAXIMA
    return multa


def calcular_fecha_devolucion(fecha_prestamo, tipo_usuario):
    """Devuelve la fecha (datetime.date) en que se debe devolver un libro.

    REQUISITO:
      - Usuarios "estudiante": 7 días corridos después del préstamo.
      - Usuarios "docente": 14 días corridos después del préstamo.
      - Si la fecha resultante cae sábado o domingo, se mueve al lunes siguiente.
      - Cualquier otro tipo de usuario debe lanzar ValueError.
    """
    # PARTE 2C: escribe primero las pruebas en tests/test_devolucion.py
    # y luego implementa esta función hasta que todas pasen.
    raise NotImplementedError("Parte 2C: implementa calcular_fecha_devolucion()")


def resumen_prestamo(titulo, dias, tipo_usuario = "estudiante"):
    """Devuelve un texto breve con el resumen de un préstamo."""
    hoy = date.today()
    fecha_limite = hoy + timedelta(days=dias)
    if tipo_usuario == None:
        tipo_usuario = "estudiante"
    texto = "Libro: " + titulo + " | Usuario: " + tipo_usuario + " | Devolver antes del: " + fecha_limite.isoformat()
    return texto
