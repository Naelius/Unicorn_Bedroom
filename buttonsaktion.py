from tkinter import messagebox, Toplevel, Label
from gif import gifwindow
from minigame import klickerspiel
from soundplayer import play_click_sound
import threading
import time

zaehlvariable = 42

# Button 1: Ändert Label-Text (du musst das Label im GUI übergeben)
def button1_action(label):
    play_click_sound()
    label.config(text='Button 1 wurde gedrückt!')

# Button 2: Öffnet kleines Fenster
def button2_action():
    play_click_sound()
    fenster = Toplevel()
    fenster.title("Neues Fenster")
    fenster.geometry("200x100")
    Label(fenster, text="Hallo! Neues Fenster geöffnet.", font=('Gothic', 12)).pack(pady=20)

# Button 3: Setzt Variable zurück und zeigt Messagebox
def button3_action():
    global zaehlvariable
    play_click_sound()
    zaehlvariable = 0
    messagebox.showinfo("Button 3", "Variable wurde zurückgesetzt!")

# Button 4: Startet Timer, der in Konsole runterzählt (oder kann angepasst werden)
def button4_action():
    play_click_sound()

    def timer():
        for i in range(5, 0, -1):
            print(f"Timer läuft: {i} Sekunden")
            time.sleep(1)
        print("Timer beendet!")

    threading.Thread(target=timer).start()
#versuch eine definition für die action
def button_action(nummer):
    play_click_sound()
    messagebox.showinfo('Hallo', f'Button {nummer} gedrückt!')

def gif_button():
    play_click_sound()
    gifwindow()

def spiel_button():
    play_click_sound()
    klickerspiel()