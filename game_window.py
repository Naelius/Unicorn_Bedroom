import tkinter as tk
from tkinter import ttk
from random import randint

class GameWindow(tk.Toplevel):
    """
    Klasse für das Mini-Spiel-Fenster.
    Diese Klasse erbt von `tk.Toplevel` und implementiert ein einfaches Zahlraten-Spiel.
    """
    def __init__(self, master):
        """
        Initialisiert das Mini-Spiel-Fenster.
        :param master: Das Hauptfenster, von dem dieses Fenster abgeleitet wird.
        """
        super().__init__(master)
        self.title("Mini-Spiel")
        self.geometry("400x300")
        self.secret = randint(1, 100)
        self.create_widgets()

    
    def create_widgets(self):
        """
        Erstellt die Widgets für das Mini-Spiel.
        Enthält ein Label, ein Eingabefeld und einen Button zum Raten der Zahl.
        """
        ttk.Label(self, text="Rate die Zahl (1-100):", font=("Arial", 14)).pack(pady=20)
        self.entry = ttk.Entry(self, font=("Arial", 14))
        self.entry.pack(pady=10)
        ttk.Button(self, text="Raten", command=self.check_guess).pack(pady=10)
        self.feedback = ttk.Label(self, text="", font=("Arial", 14))
        self.feedback.pack(pady=10)

    def check_guess(self):
        """
        Überprüft die Eingabe des Benutzers und gibt Feedback.
        Wenn die Eingabe korrekt ist, wird eine Erfolgsmeldung angezeigt,
        andernfalls wird eine Fehlermeldung angezeigt.
        """
        try:
            guess = int(self.entry.get())
            if guess == self.secret:
                self.feedback.config(text="Richtig! Gut gemacht!", foreground="green")
            elif guess < self.secret:
                self.feedback.config(text="Zu niedrig! Versuch es nochmal.", foreground="red")
            else:
                self.feedback.config(text="Zu hoch! Versuch es nochmal.", foreground="red")
        except ValueError:
            self.feedback.config(text="Bitte gib eine gültige Zahl ein.", foreground="red")
