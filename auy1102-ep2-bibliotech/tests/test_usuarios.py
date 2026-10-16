"""Pruebas de usuarios.py.

Estas pruebas deben SEGUIR PASANDO después de corregir las vulnerabilidades
de la Parte 4 (son sus pruebas de regresión).
"""
from bibliotech.usuarios import (autenticar, buscar_usuario, conectar,
                                 generar_token_sesion, registrar_usuario)


def _base_con_un_usuario():
    conexion = conectar()
    registrar_usuario(conexion, "12345678-5", "Ana Pérez", "clave-segura-1")
    return conexion


def test_registrar_y_buscar_usuario():
    conexion = _base_con_un_usuario()
    assert buscar_usuario(conexion, "12345678-5") == ("12345678-5", "Ana Pérez", "estudiante")


def test_buscar_usuario_inexistente_devuelve_none():
    conexion = _base_con_un_usuario()
    assert buscar_usuario(conexion, "11111111-1") is None


def test_autenticar_con_clave_correcta():
    conexion = _base_con_un_usuario()
    assert autenticar(conexion, "12345678-5", "clave-segura-1") is True


def test_autenticar_con_clave_incorrecta():
    conexion = _base_con_un_usuario()
    assert autenticar(conexion, "12345678-5", "otra-clave") is False


def test_token_tiene_32_caracteres_y_no_se_repite():
    assert len(generar_token_sesion()) == 32
    assert generar_token_sesion() != generar_token_sesion()


# ---------- PARTE 4: escriban aquí sus pruebas de seguridad ----------
