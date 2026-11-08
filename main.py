from pathlib import Path
from hashing import berechne_hash
from database import initialisiere_datenbank, speichere_datei, hole_hashwert


initialisiere_datenbank()
dateipfad: str = input("Geben Sie einen Dateipfad ein: ")
datei: Path = Path(dateipfad)

if datei.is_file():
    print("Datei gefunden!")
    print(f"Dateiname: {datei.name}")
    dateigroesse_bytes: int = datei.stat().st_size
    dateigroesse_kib: float = dateigroesse_bytes / 1024
    hashwert: str = berechne_hash(datei)

    speichere_datei(
        str(datei.resolve()),
        hashwert,
        dateigroesse_bytes
    )

    gespeicherter_hash: str | None = hole_hashwert(str(datei.resolve()))
    if gespeicherter_hash is None:
        print("Keine gespeicherte Referenz gefunden.")
    elif hashwert == gespeicherter_hash:
        print("Integritätsprüfung erfolgreich. Datei ist unverändert.")
    else:
        print("ACHTUNG: Datei wurde verändert!")

    print(f"SHA-256: {hashwert}")
    print(f"Dateigröße: {dateigroesse_bytes} B")
    print(f"Dateigröße: {dateigroesse_kib:.2f} KiB")
else:
    print("Datei nicht gefunden!")
