# scripts/smoke_test.py
import sqlite3

with sqlite3.connect("cigars.db") as con:
    con.row_factory = sqlite3.Row
    # Insert a sample review (price $15.00 => 1500 cents)
    con.execute("""
        INSERT INTO reviews (brand, line, vitola, country, wrapper,
                             date_smoked, rating, notes, price_cents, humidor, tags)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, ("Padron", "1964 Anniversary", "Toro", "Nicaragua", "Maduro",
          "2025-08-19", 5, "Cocoa, cedar, long finish", 1500, "TopShelf", "maduro,box-press"))

    # Read it back
    rows = con.execute("""
        SELECT id, date_smoked, brand, line, vitola, rating
        FROM reviews
        ORDER BY date_smoked DESC
        LIMIT 5
    """).fetchall()

for r in rows:
    print(dict(r))
