
import sqlite3
import pytest
import app as faultshop


def test_U01_conexion_ruta_invalida(monkeypatch, tmp_path):

    ruta_invalida = tmp_path / "carpeta_inexistente" / "shop.db"

    monkeypatch.setattr(faultshop, "DB", str(ruta_invalida))

    with pytest.raises(sqlite3.OperationalError):
        faultshop.get_db()

    assert not ruta_invalida.exists()

    print("U01: La conexion con ruta invalida fue rechazada")
