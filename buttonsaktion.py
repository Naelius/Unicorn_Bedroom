from tkinter import messagebox
from gif import gifwindow
from minigame import klickerspiel
from soundplayer import play_click_sound

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