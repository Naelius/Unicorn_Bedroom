import tkinter as tk

def klickerspiel():
    fenster = tk.Toplevel()
    fenster.title("Klickerspiel")
    fenster.geometry('500x500')

    punktzahl = tk.IntVar(value=0)

    punktelabel = tk.Label(fenster, textvariable=punktzahl, font=('Gothic', 14))
    punktelabel.pack(pady=20)

    def klick():
        punktzahl.set(punktzahl.get() + 1)

    klickbutton = tk.Button(fenster, text='Klickerhero', command=klick, font=('Gothic', 14))
    klickbutton.pack(pady=10)