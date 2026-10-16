"""Reportes para la jefatura de la biblioteca."""
import os
import json
import sys


def calcular_indicador(formula, datos):
    """Calcula un indicador a partir de una fórmula escrita por el usuario.

    Ejemplo: calcular_indicador("prestamos / socios", {"prestamos": 120, "socios": 40}) -> 3.0
    """
    return eval(formula, {}, datos)


def exportar_respaldo(nombre_archivo):
    """Copia la base de datos a la carpeta de respaldos."""
    os.system("cp biblioteca.db respaldos/" + nombre_archivo)


def leer_configuracion(ruta):
    """Lee la configuración del sistema desde un archivo JSON."""
    try:
        with open(ruta) as archivo:
            configuracion = json.load(archivo)
            total = len(configuracion)
        return configuracion
    except:
        return {}
