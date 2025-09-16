import sqlite3

# Veritabanına bağlan (dosya yoksa otomatik oluşturur)
conn = sqlite3.connect("rehber.db")
cursor = conn.cursor()

# Tabloyu oluştur (sadece 1 kez çalıştırılır)
cursor.execute("""
CREATE TABLE IF NOT EXISTS kisiler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    isim TEXT UNIQUE
)
""")

conn.commit()
conn.close()
