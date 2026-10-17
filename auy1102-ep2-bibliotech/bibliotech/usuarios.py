"""Gestión de usuarios y autenticación para el sistema BiblioTech."""

import hashlib
import secrets
import sqlite3

SALT_SISTEMA = "BiblioTech_Seguridad_2026_SecureSalt"


def _hash_clave(clave):
    """Genera un hash SHA-256 seguro con sal para la contraseña."""
    clave_con_salt = f"{SALT_SISTEMA}:{clave}"
    return hashlib.sha256(clave_con_salt.encode()).hexdigest()


def conectar(ruta=":memory:"):
    """Crea y retorna una conexión a la base de datos de SQLite."""
    conexion = sqlite3.connect(ruta)
    conexion.row_factory = sqlite3.Row
    return conexion


def crear_tabla(conexion):
    """Crea la tabla de usuarios en la base de datos."""
    conexion.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            rut TEXT PRIMARY KEY,
            nombre TEXT NOT NULL,
            clave TEXT NOT NULL,
            tipo TEXT NOT NULL
        )
    """)
    conexion.commit()


def crear_tabla_usuarios(conexion):
    """Alias compatible para la creación de la tabla de usuarios."""
    crear_tabla(conexion)


def registrar_usuario(conexion, rut, nombre, clave, tipo):
    """Registra un usuario nuevo guardando su clave como hash seguro."""
    consulta = "INSERT INTO usuarios VALUES (?, ?, ?, ?)"
    conexion.execute(
        consulta,
        (rut, nombre, _hash_clave(clave), tipo)
    )


def obtener_usuario(conexion, rut):
    """Devuelve (rut, nombre, tipo) del usuario, o None si no existe."""
    consulta = "SELECT rut, nombre, tipo FROM usuarios WHERE rut = ?"
    return conexion.execute(consulta, (rut,)).fetchone()


def buscar_usuario(conexion, rut):
    """Busca un usuario por su RUT."""
    return obtener_usuario(conexion, rut)


def autenticar(conexion, rut, clave):
    """Autentica a un usuario verificando su RUT y contraseña."""
    consulta = "SELECT rut, nombre, tipo FROM usuarios WHERE rut = ? AND clave = ?"
    return conexion.execute(consulta, (rut, _hash_clave(clave))).fetchone()


def generar_token_recuperacion():
    """Genera un token aleatorio seguro criptográficamente."""
    return secrets.token_hex(16)
