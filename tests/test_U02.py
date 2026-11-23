"""U02 - Conexion valida con SQLite (original, Esteban)."""
import sqlite3
import app as faultshop


def test_U02_conexion_valida(tmp_path, monkeypatch):
    ruta = tmp_path / "base_esteban_u02.db"
    monkeypatch.setattr(faultshop, "DB", str(ruta))

    conexion = faultshop.get_db()
    try:
        assert isinstance(conexion, sqlite3.Connection)
        assert ruta.is_file()
        fila = conexion.execute("SELECT 1 AS numero").fetchone()
        assert fila["numero"] == 1
        print("U02: conexion valida y consulta de prueba satisfactoria")
    finally:
        conexion.close()
