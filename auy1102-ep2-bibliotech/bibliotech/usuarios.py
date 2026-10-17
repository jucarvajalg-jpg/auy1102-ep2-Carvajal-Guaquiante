"""Gestión de usuarios y autenticación para el sistema BiblioTech."""

import hashlib
import secrets

SALT_SISTEMA = "BiblioTech_Seguridad_2026_SecureSalt"


def _hash_clave(clave):
    """Genera un hash SHA-256 con sal (salt) para prevenir ataques por tablas arcoíris."""
    clave_con_salt = f"{SALT_SISTEMA}:{clave}"
    return hashlib.sha256(clave_con_salt.encode()).hexdigest()


def registrar_usuario(conexion, rut, nombre, clave, tipo):
    """Registra un usuario nuevo guardando su clave como hash seguro con sal."""
    consulta = "INSERT INTO usuarios VALUES (?, ?, ?, ?)"
    conexion.execute(
        consulta,
        (rut, nombre, _hash_clave(clave), tipo)
    )


def obtener_usuario(conexion, rut):
    """Devuelve (rut, nombre, tipo) del usuario, o None si no existe."""
    consulta = "SELECT rut, nombre, tipo FROM usuarios WHERE rut = ?"
    return conexion.execute(consulta, (rut,)).fetchone()


def generar_token_recuperacion():
    """Genera un token aleatorio seguro criptográficamente."""
    return secrets.token_hex(16)
