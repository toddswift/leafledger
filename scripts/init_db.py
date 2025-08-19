import sqlite3 
from pathlib import Path

DB_PATH = Path("cigars.db")

CREATE_SQL = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS reviews (
  id          INTEGER PRIMARY KEY,
  brand       TEXT NOT NULL,
  line        TEXT,
  vitola      TEXT,
  country     TEXT,
  wrapper     TEXT,
  binder      TEXT,
  filler      TEXT,

  date_smoked TEXT NOT NULL,                         -- "YYYY-MM-DD"
  rating      INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
  notes       TEXT,
  price_cents INTEGER,                               -- store money as integer cents
  humidor     TEXT,
  tags        TEXT,                                  -- CSV e.g. "maduro,box-press"

  created_at  TEXT NOT NULL DEFAULT (datetime('now')),
  updated_at  TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_reviews_brand       ON reviews(brand);
CREATE INDEX IF NOT EXISTS idx_reviews_country     ON reviews(country);
CREATE INDEX IF NOT EXISTS idx_reviews_rating      ON reviews(rating);
CREATE INDEX IF NOT EXISTS idx_reviews_date        ON reviews(date_smoked);

CREATE TRIGGER IF NOT EXISTS trg_reviews_updated_at
AFTER UPDATE ON reviews
FOR EACH ROW
BEGIN
  UPDATE reviews SET updated_at = datetime('now') WHERE id = OLD.id;
END;
"""

def init_db():
    # create file and schema
    with sqlite3.connect(DB_PATH) as con:
        con.row_factory = sqlite3.Row
        con.executescript(CREATE_SQL)
        # Optional: WAL for nicer write behavior in future
        con.execute("PRAGMA journal_mode = WAL")

if __name__ == "__main__":
    init_db()
    print(f"Database initialized at {DB_PATH.resolve()}")