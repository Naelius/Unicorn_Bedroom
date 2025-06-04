import tkinter as tk
import random

def start_minigame(parent):
    game_win = tk.Toplevel(parent)
    game_win.title("Zufallszahl raten")

    number = random.randint(1, 10)
    tk.Label(game_win, text="Rate eine Zahl zwischen 1 und 10:").pack()
    entry = tk.Entry(game_win)
    entry.pack()

    result = tk.Label(game_win, text="")
    result.pack()

    def guess():
        try:
            guess = int(entry.get())
            if guess == number:
                result.config(text="Richtig!", fg="green")
            else:
                result.config(text=f"Falsch! Die Zahl war {number}", fg="red")
        except:
            result.config(text="Bitte eine gültige Zahl eingeben.", fg="orange")

    tk.Button(game_win, text="Raten", command=guess).pack()