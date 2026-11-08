# TraceCheck – Datei-Integritätsprüfung

Ein kleines Python-Lernprojekt mit SHA-256 und SQLite, entstanden im Rahmen meiner Einarbeitung in die Grundlagen der digitalen Forensik.

Das Programm berechnet SHA-256-Hashwerte von Dateien, speichert Referenzwerte in SQLite und vergleicht sie bei späteren Prüfungen. Es ist **kein professionelles forensisches Beweissicherungswerkzeug**.

## Lokal starten

Python 3.10+ wird benötigt. Im Projektordner:

```powershell
python -m pip install -r requirements.txt
```

**Konsolenversion:**

```powershell
python main.py
```

Danach einen Dateipfad eingeben. Bei der ersten Untersuchung wird eine Referenz in SQLite gespeichert, bei weiteren Untersuchungen desselben Pfads werden die Hashwerte verglichen.

**Lokale Weboberfläche:**

```powershell
python -m flask --app app run
```

Im Browser `http://127.0.0.1:5000` öffnen, eine Datei auswählen und „Registrieren“ oder „Integrität prüfen“ anklicken.

Die Weboberfläche nutzt `web:` plus Dateiname als lokale Zuordnung. Unterschiedliche Uploads mit demselben Dateinamen gelten deshalb als dieselbe Referenz. Keine öffentliche Online-Demo; die Anwendung ist für die lokale Nutzung gedacht.

## Dateien

- `main.py` – Konsolenversion
- `hashing.py` – SHA-256 (Dateipfad und Upload-Stream)
- `database.py` – SQLite-Zugriff
- `app.py` – Flask für die lokale HTML-Oberfläche
- `templates/index.html`, `static/style.css` – Retro-Design

## Datenbank

`datei_detektiv.db` wird beim Start erstellt, wenn sie nicht existiert. Sie liegt lokal im Projektordner und enthält Dateipfade bzw. Dateinamen, Hashwerte, Dateigrößen und Zeitpunkte.

Die Datenbank ist durch `.gitignore` vom GitHub-Repository ausgeschlossen. Eine lokal bereits vorhandene Datenbank kann weiterverwendet werden. **Bitte keine lokalen Datenbankdateien mit persönlichen Dateipfaden öffentlich hochladen.**

Zum Zurücksetzen die Anwendung beenden und die lokale `datei_detektiv.db` löschen; beim nächsten Start wird sie neu erstellt.
