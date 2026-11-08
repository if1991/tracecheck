from pathlib import Path
import hashlib
from typing import BinaryIO


def berechne_hash(datei: Path) -> str:
    x = hashlib.sha256()

    with datei.open("rb") as thisDatei:
        while True:
            daten = thisDatei.read(16)
            if daten == b"":
                break
            x.update(daten)

    return x.hexdigest()


def berechne_hash_stream(stream: BinaryIO) -> str:
    x = hashlib.sha256()

    while True:
        daten = stream.read(65536)
        if daten == b"":
            break
        x.update(daten)

    return x.hexdigest()
