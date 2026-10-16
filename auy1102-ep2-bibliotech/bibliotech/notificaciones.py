"""Envío de avisos de vencimiento por correo y por webhook.

Este módulo no se ejecuta en las pruebas: se usa en producción.
"""
import requests
from jinja2 import Environment

PLANTILLA = "Hola {{ nombre }}, tu libro '{{ titulo }}' vence el {{ fecha }}."


def armar_mensaje(nombre, titulo, fecha):
    entorno = Environment()
    return entorno.from_string(PLANTILLA).render(nombre=nombre, titulo=titulo, fecha=fecha)


def enviar_aviso(url_webhook, mensaje):
    respuesta = requests.post(url_webhook, json={"texto": mensaje})
    return respuesta.status_code == 200
