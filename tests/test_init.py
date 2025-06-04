import os
import sqlite3
import pytest
import tempfile
import shutil

from homecash.transactions import init_db


def test_db_schema():
    # Usar un archivo temporal para la base de datos
    temp_dir = tempfile.mkdtemp()
    db_path = os.path.join(temp_dir, "test_homecash.db")
    orig_db_path = init_db.DB_PATH
    init_db.DB_PATH = db_path
    try:
        init_db.init_db()
        conn = sqlite3.connect(db_path)
        cursor = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='transactions';"
        )
        assert cursor.fetchone() is not None, "La tabla 'transactions' no fue creada"
    finally:
        init_db.DB_PATH = orig_db_path
        shutil.rmtree(temp_dir)
