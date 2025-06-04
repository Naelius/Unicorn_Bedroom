# Unicorn_Bedroom

Ein spielerisches Python-GUI-Projekt mit Einhorn-Charme, Animationen, Sound und einem kleinen Ratespiel.

## Übersicht

Dieses Projekt ist eine Desktop-Anwendung mit einer grafischen Benutzeroberfläche (GUI) auf Basis von `tkinter`. Es bietet verschiedene interaktive Funktionen, Animationen und Soundeffekte.

## Dateien und Ordner

- **main.py**  
  Startpunkt der Anwendung. Initialisiert das Hauptfenster.

- **ui_main.py**  
  Definiert das Haupt-GUI-Fenster mit Buttons für verschiedene Aktionen (Hallo sagen, Info anzeigen, Fenster bewegen, Hintergrund ändern, Animation anzeigen, Mini-Spiel starten).

- **actions.py**  
  Enthält Funktionen für die Buttons, z.B. Begrüßung, Info-Dialog, Fenster bewegen, Hintergrundfarbe ändern. Spielt jeweils einen Soundeffekt ab.

- **sound.py**  
  Stellt die Funktion `play_sound` bereit, um Soundeffekte (z.B. Klicks) mit `pygame` abzuspielen.

- **animation_window.py**  
  Öffnet ein neues Fenster und zeigt eine animierte GIF-Datei an.

- **game_window.py**  
  Öffnet ein Mini-Spiel (Zahlenraten) in einem eigenen Fenster.

- **assets/**  
  Enthält Ressourcen wie:
  - **animation.gif**: Die Animation für das Animationsfenster.
  - **click.mp3**: Soundeffekt für Button-Klicks.
  - **animation.py**: (Derzeit leer, kann für zukünftige Animationen genutzt werden.)

- **README.md**  
  Diese Datei. Enthält eine Übersicht und Anleitung.

- **.gitignore**  
  Ignoriert temporäre und Build-Dateien für Git.

## Voraussetzungen

- Python 3.x
- Abhängigkeiten:  
  - `tkinter` (Standard bei Python)
  - `pygame` (für Sound)
  - `Pillow` (für GIF-Animationen)

Installiere fehlende Pakete ggf. mit:

pip install pygame pillow
