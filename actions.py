from tkinter import messagebox
from sound import play_sound

def say_hello():
    """
    Zeigt eine Nachricht an und spielt einen Sound ab.
    Diese Funktion wird aufgerufen, wenn der "Sag Hallo"-Button geklickt wird.
    """
    print("Hallo Welt!")
    play_sound("assets/click.mp3")

def show_info():
    """
    Zeigt eine Informationsnachricht an und spielt einen Sound ab.
    Diese Funktion wird aufgerufen, wenn der "Zeige Info"-Button geklickt wird.
    """
    messagebox.showinfo("Info", "Hier könnte deine Info stehen!")
    play_sound("assets/click.mp3")

def move_window(window):
    """
    Bewegt das Fenster an eine neue Position und spielt einen Sound ab.
    Diese Funktion wird aufgerufen, wenn der "Bewege Fenster"-Button geklickt wird.
    :param window: Das Fenster, das bewegt werden soll.
    """
    window.geometry("+300+300")  # Move the window to a new position
    play_sound("assets/click.mp3")

def change_bg(window):
    """
    Ändert die Hintergrundfarbe des Fensters und spielt einen Sound ab.
    Diese Funktion wird aufgerufen, wenn der "Hintergrund ändern"-Button geklickt wird.
    :param window: Das Fenster, dessen Hintergrundfarbe geändert werden soll.
    """
    window.configure(bg="#ffd180")  # Change the background color of the window
    play_sound("assets/click.mp3")