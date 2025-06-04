import tkinter as tk
from tkinter import ttk
from actions import say_hello, show_info, move_window, change_bg
from animation_window import AnimationWindow
from game_window import GameWindow

class MainApp(tk.Tk):
    """
    Hauptanwendungsklasse für die GUI-Anwendung.
    Diese Klasse erbt von `tk.Tk` und initialisiert die Anwendung mit einem Titel,
    einer Größe und einem Hintergrund. Sie enthält auch die Logik zum Erstellen der Widgets.
    """
    def __init__(self):
        """
        Initialisiert die Hauptanwendung.
        Setzt den Titel, die Größe und den Hintergrund der Anwendung.
        """
        super().__init__()
        self.title("Spielerische GUI-Anwendung")
        self.geometry("600x500")
        self.configure(bg="#e0f7fa")

        self.create_widgets()

    def create_widgets(self):
        """
        Erstellt die Widgets der Anwendung.
        Enthält Buttons für verschiedene Aktionen und ein zentrales Container-Widget.
        """
        container = tk.Frame(self, bg="#e0f7fa")
        container.place(relx=0.5, rely=0.5, anchor="center")  # Zentrierung

        title = ttk.Label(container, text="Einhornliche Grüße!", font=("Arial", 18))
        title.pack(pady=20)

        buttons = [
            ("Sag Hallo", "#ff9999", say_hello),
            ("Zeige Info", "#99ff99", show_info),
            ("Bewege Fenster", "#9999ff", lambda: move_window(self)),
            ("Hintergrund ändern", "#ffcc99", lambda: change_bg(self)),
            ("Animation anzeigen", "#cc99ff", lambda: AnimationWindow(self)),
            ("Mini-Spiel starten", "#ffff99", lambda: GameWindow(self))
        ]

        for text, color, command in buttons:
            btn = tk.Button(container, text=text, bg=color, width=25, height=2, command=command)
            btn.pack(pady=5)
