import tkinter as tk
from tkinter import messagebox

def add_menue(fenster):
    menuleiste = tk.Menu(fenster)

    #Datei-Menü 
    datei_menu = tk.Menu(menuleiste, tearoff=0)
    datei_menu.add_command(label='Beenden', command=fenster.quit)
    menuleiste.add_cascade(label='Datei', menu=datei_menu)


    #info-Menü
    info_menu = tk.Menu(menuleiste, tearoff=0)
    info_menu.add_command(label='Über', command=lambda: messagebox.showinfo('Über', 'Button Anwendung v1.0\nErstellt von Gotty'))
    menuleiste.add_cascade(label='Info', menu=info_menu)

    fenster.config(menu=menuleiste)
