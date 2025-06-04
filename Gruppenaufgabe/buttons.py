import tkinter as tk
from tkinter import ttk, messagebox, Menu, Toplevel
from tkinter import filedialog
from PIL import Image, ImageTk, ImageSequence
import threading
import random
import time
import pygame

# Initialisiere pygame für Sound\pygame.init()

# Sounddatei-Pfad (ersetzen durch echte Datei)
sound_file = "click.wav"

# Hauptanwendungsklasse
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Python GUI Anwendung")
        self.root.geometry("600x400")

        self.create_menu()
        self.create_widgets()
        self.create_status_bar()

        # Fortschrittsbalken starten
        self.progress()

    def create_menu(self):
        menu_bar = Menu(self.root)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Öffnen", command=self.dummy_action)
        file_menu.add_command(label="Beenden", command=self.root.quit)
        menu_bar.add_cascade(label="Datei", menu=file_menu)

        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Info", command=lambda: messagebox.showinfo("Info", "Dies ist eine Demo-GUI in Python."))
        menu_bar.add_cascade(label="Hilfe", menu=help_menu)

        self.root.config(menu=menu_bar)

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(fill="both", expand=True)

        self.buttons = [
            ("Zeige Nachricht", "lightblue", self.show_message),
            ("Öffne GIF", "lightgreen", self.open_gif_window),
            ("Starte Spiel", "lightcoral", self.open_game_window),
            ("Farbwechsel", "lightyellow", self.change_color),
            ("Fortschritt", "lightsalmon", self.progress),
            ("Beenden", "lightgray", self.root.quit)
        ]

        for i, (text, color, cmd) in enumerate(self.buttons):
            btn = tk.Button(frame, text=text, bg=color, width=20, height=2, command=lambda c=cmd: self.play_sound(c))
            btn.grid(row=i // 2, column=i % 2, padx=10, pady=10, sticky="nsew")

        for i in range(3):
            frame.rowconfigure(i, weight=1)
        for i in range(2):
            frame.columnconfigure(i, weight=1)

    def play_sound(self, func):
        try:
            pygame.mixer.Sound(sound_file).play()
        except:
            pass  # Sound optional, bei Fehler nichts tun
        func()

    def show_message(self):
        messagebox.showinfo("Nachricht", "Dies ist eine Beispielnachricht!")

    def open_gif_window(self):
        win = Toplevel(self.root)
        win.title("Animation")
        lbl = tk.Label(win)
        lbl.pack()

        gif_path = "animation.gif"  # Ersetze durch eigenen Pfad

        try:
            im = Image.open(gif_path)
            frames = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(im)]

            def animate(counter=0):
                lbl.configure(image=frames[counter])
                win.after(100, animate, (counter + 1) % len(frames))

            animate()
        except:
            tk.Label(win, text="GIF konnte nicht geladen werden.").pack()

    def open_game_window(self):
        win = Toplevel(self.root)
        win.title("Zufallszahl raten")
        tk.Label(win, text="Rate eine Zahl von 1 bis 10").pack(pady=10)

        number = random.randint(1, 10)

        entry = tk.Entry(win)
        entry.pack()

        result_lbl = tk.Label(win, text="")
        result_lbl.pack(pady=5)

        def check_guess():
            try:
                guess = int(entry.get())
                if guess == number:
                    result_lbl.config(text="Richtig!")
                else:
                    result_lbl.config(text="Falsch! Versuche es erneut.")
            except:
                result_lbl.config(text="Bitte gib eine Zahl ein.")

        tk.Button(win, text="Prüfen", command=check_guess).pack(pady=5)

    def change_color(self):
        colors = ["#ff9999", "#99ff99", "#9999ff", "#ffff99"]
        self.root.configure(bg=random.choice(colors))

    def create_status_bar(self):
        self.status = tk.Label(self.root, text="Bereit", bd=1, relief="sunken", anchor="w")
        self.status.pack(side="bottom", fill="x")

    def progress(self):
        def update():
            for i in range(101):
                self.status.config(text=f"Lade... {i}%")
                time.sleep(0.01)
            self.status.config(text="Bereit")

        threading.Thread(target=update, daemon=True).start()

    def dummy_action(self):
        messagebox.showinfo("Datei", "Datei öffnen Funktion (noch nicht implementiert).")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
