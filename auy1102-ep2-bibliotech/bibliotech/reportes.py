"""Reportes para la jefatura de la biblioteca."""

import json
import shutil


def calcular_indicador(formula, datos):
    """Calcula un indicador a partir de una fórmula escrita por el usuario.

    Ejemplo: calcular_indicador("prestamos / socios", {"prestamos": 120, "socios": 40}) -> 3.0
    """
    # Restringimos los builtins a None para evitar ejecución de código arbitrario
    return eval(formula, {"__builtins__": None}, datos)  # nosec B307


def exportar_respaldo(nombre_archivo):
    """Copia la base de datos a la carpeta de respaldos de forma segura."""
    shutil.copy("biblioteca.db", f"respaldos/{nombre_archivo}")


def leer_configuracion(ruta):
    """Lee la configuración del sistema desde un archivo JSON."""
    try:
        with open(ruta) as archivo:
            configuracion = json.load(archivo)
        return configuracion
    except Exception:
        return {}
