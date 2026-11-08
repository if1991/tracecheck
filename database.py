import sqlite3

# Initialisierung der Tabelle

def initialisiere_datenbank() -> None:
    verbindung = sqlite3.connect("datei_detektiv.db")
    print("Datenbankverbindung hergestellt!")

    verbindung.execute("""
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY,
            file_path TEXT NOT NULL UNIQUE,
            sha256 TEXT NOT NULL,
            size_bytes INTEGER NOT NULL,
            registered_at TEXT NOT NULL
        )
    """)
    verbindung.commit()
    verbindung.close()


# Dateien speichern

def speichere_datei(dateipfad: str, hashwert: str, groesse: int) -> bool:
    verbindung = sqlite3.connect("datei_detektiv.db")
    ergebnis = verbindung.execute(
        "SELECT 1 FROM files WHERE file_path = ?",
        (dateipfad,)
    )
    eintrag = ergebnis.fetchone()

    if eintrag is not None:
        print("Datei ist bereits registriert")
        verbindung.close()
        return False

    verbindung.execute("""
        INSERT INTO files (file_path, sha256, size_bytes, registered_at)
        VALUES (?, ?, ?, CURRENT_TIMESTAMP)
    """, (dateipfad, hashwert, groesse))

    verbindung.commit()
    verbindung.close()
    return True


# Hashwert holen

def hole_hashwert(dateipfad: str) -> str | None:
    verbindung = sqlite3.connect("datei_detektiv.db")
    ergebnis = verbindung.execute(
        "SELECT sha256 FROM files WHERE file_path = ?",
        (dateipfad,)
    )
    eintrag = ergebnis.fetchone()
    verbindung.close()

    if eintrag is None:
        return None
    return eintrag[0]
