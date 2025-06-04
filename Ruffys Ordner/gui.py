import tkinter as tk
from tkinter import messagebox, Toplevel, Menu
from tkinter.ttk import Progressbar
import threading
import time
from animation import AnimatedGIF
from minigame import start_minigame
from sound import play_click_sound

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Python GUI Anwendung")
        self.root.geometry("600x400")
        self.create_widgets()
        self.create_menu()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True, fill="both")

        self.status = tk.Label(self.root, text="Bereit", bd=1, relief="sunken", anchor="w")
        self.status.pack(side="bottom", fill="x")

        self.progress = Progressbar(self.root, orient="horizontal", length=100, mode="determinate")
        self.progress.pack(side="bottom", pady=5)

        btn_texts = [
            ("Info zeigen", self.show_info),
            ("Fenster öffnen", self.open_window),
            ("Mini-Spiel starten", self.start_minigame),
            ("Fortschritt starten", self.start_progress),
            ("Nachricht anzeigen", self.show_message),
            ("Beenden", self.root.quit)
        ]

        colors = ["red", "green", "blue", "orange", "purple", "cyan"]

        for i, (text, command) in enumerate(btn_texts):
            btn = tk.Button(self.frame, text=text, command=lambda c=command: [c(), play_click_sound()], 
                            bg=colors[i], fg="white", height=2, width=20)
            btn.grid(row=i//2, column=i%2, padx=10, pady=10, sticky="nsew")

        for i in range(3):
            self.frame.rowconfigure(i, weight=1)
        for i in range(2):
            self.frame.columnconfigure(i, weight=1)

    def create_menu(self):
        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Beenden", command=self.root.quit)
        menubar.add_cascade(label="Datei", menu=filemenu)

        infomenu = Menu(menubar, tearoff=0)
        infomenu.add_command(label="Über", command=lambda: messagebox.showinfo("Über", "Diese Anwendung wurde in Python erstellt."))
        menubar.add_cascade(label="Info", menu=infomenu)

        self.root.config(menu=menubar)

    def show_info(self):
        self.status.config(text="Info-Button gedrückt")
        messagebox.showinfo("Info", "Dies ist eine Beispiel-GUI-Anwendung.")

    def open_window(self):
        self.status.config(text="Fenster mit Animation geöffnet")
        win = Toplevel(self.root)
        win.title("Animation")
        anim = AnimatedGIF(win, "animation.gif")
        anim.pack()

    def show_message(self):
        self.status.config(text="Nachricht angezeigt")
        messagebox.showwarning("Warnung", "Dies ist eine Warnmeldung!")

    def start_progress(self):
        self.status.config(text="Fortschritt läuft")

        def run():
            self.progress["value"] = 0
            for i in range(101):
                time.sleep(0.03)
                self.progress["value"] = i
            self.status.config(text="Bereit")

        threading.Thread(target=run).start()

    def start_minigame(self):
        self.status.config(text="Mini-Spiel gestartet")
        start_minigame(self.root)
