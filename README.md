# Projekt Setup für das WPF Data Mining (SO_2024)

## Voraussetzungen
- Python
- Git
- Virtual

## Installation
1. Klone das Repo
```
git clone https://github.com/bogdankrenz/data_mining_SO2024.git
cd data_mining_SO2024
```
2. Erstelle und aktiviere eine virtuelle Umgebung
```
python -m venv env
# On Windows:
.\env\Scripts\activate
# On macOS/Linux:
source env/bin/activate
```
3. Installiere die Abhängigkeiten
```
pip install -r requirements.txt
```

## Testen vom Setup
1. Führe das Testskript aus, um sicherzustellen, dass alle Abhängigkeiten korrekt installiert sind
- Alternativ kann man das Script mit python3 ausführen falls eine andere installation vorhanden ist
```
# Teste das eine oder andere
python src/test_setup.py

python3 src/test_setup.py
```
Dieses Skript überprüft die Installation von NumPy, Pandas und Matplotlib und erstellt einen einfachen Plot mit dem Namen test_plot.png.

2. Öffne das Jupyter Notebook, um die Integration zu überprüfen:
```
jupyter notebook notebooks/test_notebook.ipynb
```

## Ordner Struktur
```
data-mining
├── LICENSE
├── README.md
├── data
│   ├── external            # Externe Daten/Statistiken außerhalb des Projektes
│   ├── processed           # Verarbeitete Daten
│   └── raw                 # Daten die wir bekommen haben im Ausgagnszustand
│       ├── emp_df.pkl
│       ├── exchange_rates_df.pkl
│       ├── production_index_detail.xlsx
│       ├── production_index_df.pkl
│       └── wages_df.pkl
├── notebooks
├── requirements.txt
├── setup.py
├── src                     # Unser Code
└── tests                   # Für Leute die extra fancy sind und tests schreiben wollen :D
```
## Workflow

**Der Main Branch ist unsere SOURCE OF TRUTH**
Im main liegen Daten/Code welche durch eine Review gegangen sind und **funktionieren**

Wenn ihr an euren Aufgaben arbeiten wollt, erstellt einen Branch vom main aus.
Sobald ihr fertig seid, pusht den Branch mit den Commits ins Github hoch und erstellt ein MR.

Bei 4 Leute wäre es cool wenn bei einem Review 2 Leute das Ok geben damit die Sachen in den Main landen.
Bei 3 Leuten reichts wenn es nur eine andere Person absegnet.

Schreibt kurz ins MR was die Änderungen sind und was das Ziel der Changes ist.
Kommentare und saubere Commit Messages sind gern gesehen.

# TODO's
- Remove .placeholder.txt once every directory has at least one file so git can keep tracking them
