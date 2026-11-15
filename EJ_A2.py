import pdfplumber
import re
import tkinter as tk
from tkinter import filedialog

print("--- M&A Dokumenten-Analyzer ---")
print("Öffne Dateiauswahl-Fenster... Bitte wähle eine PDF aus.")

# Ein unsichtbares Hauptfenster erstellen, damit sich nur der Datei-Explorer öffnet
root = tk.Tk()
root.withdraw()

# Das grafische Dateiauswahl-Fenster öffnen
dateipfad = filedialog.askopenfilename(
    title="Wähle eine PDF-Datei aus",
    filetypes=[("PDF Dateien", "*.pdf"), ("Alle Dateien", "*.*")]
)

# Prüfen, ob der Nutzer eine Datei ausgewählt oder abgebrochen hat
if not dateipfad:
  print("❌ Keine Datei ausgewählt. Das Programm wurde abgebrochen.")
else:
  print(f"\nAnalysiere Dokument: {dateipfad} ... Bitte warten...\n")

  ergebnisse = []
  max_laenge = 0
  gefundene_insights = 0

  # PDF seitenweise öffnen und analysieren
  with pdfplumber.open(dateipfad) as pdf:
    for seiten_index, seite in enumerate(pdf.pages):
      text = seite.extract_text()
      if text:
        bereinigter_text = text.replace("\n", " ")
        saetze = re.split(r'(?<=[.!?])\s+', bereinigter_text)

        for satz in saetze:
          # Sätze filtern, die Zahlen mit Apostroph/Punkt oder CHF enthalten
          if re.search(r"\d+['\.]\d+", satz) or "CHF" in satz:
            gefundene_insights += 1
            seiten_nummer = seiten_index + 1

            zeile = (
                f"[{gefundene_insights}] (Seite {seiten_nummer})"
                f" 💡 {satz.strip()}"
            )
            ergebnisse.append(zeile)

            if len(zeile) > max_laenge:
              max_laenge = len(zeile)

  if gefundene_insights == 0:
    print(
        "⚠️ Keine passenden Finanzwerte oder Kennzahlen in diesem Dokument"
        " gefunden."
    )
  else:
    print("--- Automatisch extrahierte Finanz-Insights ---")
    print("=" * max_laenge)

    for zeile in ergebnisse:
      print(zeile)
      print("_" * max_laenge)