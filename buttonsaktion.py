from tkinter import messagebox
from gif import gifwindow

#versuch eine definition für die action
def button_action(nummer):
    messagebox.showinfo('Hallo', f'Button {nummer} gedrückt!')

def gif_button():
    gifwindow()