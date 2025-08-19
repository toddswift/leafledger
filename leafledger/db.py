import sqlite3
from pathlib import Path

DB_PATH = Path("cigars.db")

CREATE_SQL = """  -- paste the same CREATE_SQL from init_db.py here  """

def connect(db_path: Path = DB_PATH):
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON")
    con.execute("PRAGMA journal_mode = WAL")
    return con

def init_db(db_path: Path = DB_PATH):
    with connect(db_path) as con:
        con.executescript(CREATE_SQL)
