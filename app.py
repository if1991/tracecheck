from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from hashing import berechne_hash_stream
from database import initialisiere_datenbank, speichere_datei, hole_hashwert

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024
initialisiere_datenbank()


@app.route("/", methods=["GET", "POST"])
def startseite():
    meldung: str = "Bereit für Dateianalyse..."

    if request.method == "POST":
        datei = request.files.get("file")
        aktion = request.form.get("aktion")

        if datei is None or datei.filename == "":
            meldung = "FEHLER: Keine Datei ausgewählt!"
        else:
            dateiname = secure_filename(datei.filename)
            if not dateiname:
                meldung = "FEHLER: Ungültiger Dateiname!"
            else:
                hashwert = berechne_hash_stream(datei.stream)
                dateipfad = "web:" + dateiname

                if aktion == "registrieren":
                    gespeichert = speichere_datei(dateipfad, hashwert, datei.stream.tell())
                    if gespeichert:
                        meldung = f"REGISTRIERT: {dateiname} | SHA-256: {hashwert}"
                    else:
                        meldung = f"Datei bereits registriert: {dateiname}"
                elif aktion == "pruefen":
                    referenz = hole_hashwert(dateipfad)
                    if referenz is None:
                        meldung = "Datei noch nicht registriert!"
                    elif hashwert == referenz:
                        meldung = "Integritätsprüfung erfolgreich. Datei ist unverändert."
                    else:
                        meldung = "ACHTUNG: Datei wurde verändert!"

    return render_template("index.html", meldung=meldung)
