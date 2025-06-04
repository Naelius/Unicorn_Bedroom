import tkinter as tk
from tkinter import Toplevel
from tkinter import messagebox
import random
import itertools

#hauptfenster machen 

root = tk.Tk()
root.title('Button Anwendung')
root.geometry('600x600')
root.configure(bg='lightgray')


#versuch eine definition für die action
def button_action(nummer):
    messagebox.showinfo('Hallo', f'Button {nummer} gedrückt!')

#bruachte liste für die farben 
farben = ['red', 'green', 'blue', 'orange', 'purple', 'cyan']


#lambda funktion einfach als fake funktion 
funktionen = [ lambda: button_action(1), lambda: button_action(2), lambda: button_action(3), lambda: button_action(4), lambda: button_action(5), lambda: button_action(6)]



#irgendwie ne for schleife herstellen um buttons zu erstellen
for i, (farbe, funktion) in enumerate(zip(farben, funktionen)):
    button = tk.Button(
        root, text=F'Button {i+1}', bg=farbe, fg='white', command=funktion, font=('Gothic', 12), 
        width=15, height=2
    )
    button.pack(padx=5, pady=5, side='left')



root.mainloop()
