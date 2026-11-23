import sqlite3

import app as faultshop


def test_U07_get_db_returns_rows_accessible_by_column_name(tmp_path, monkeypatch):
    database_path = tmp_path / "test_shop.db"
    monkeypatch.setattr(faultshop, "DB", str(database_path))

    connection = faultshop.get_db()
    try:
        assert connection.row_factory is sqlite3.Row

        connection.execute("CREATE TABLE products (id INTEGER, name TEXT)")
        connection.execute(
            "INSERT INTO products (id, name) VALUES (?, ?)",
            (7, "Teclado"),
        )
        row = connection.execute("SELECT id, name FROM products").fetchone()

        assert row["id"] == 7
        assert row["name"] == "Teclado"
    finally:
        connection.close()