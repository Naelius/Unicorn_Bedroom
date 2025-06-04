import tkinter as tk

def klickerspiel():
    fenster = tk.Toplevel()
    fenster.title("Klickerspiel")
    fenster.geometry('500x500')

    punktzahl = tk.IntVar(value=0)
    zeit = tk.IntVar(value=10) #timer für 10 Sekunden

    #punkteanzeige
    punktelabel = tk.Label(fenster, textvariable=punktzahl, font=('Gothic', 14))
    punktelabel.pack(pady=20)

    #timeranzeige
    zeitlabel = tk.Label(fenster, text=F'Zeit: {zeit.get()} Sekunden', font=('Gothic', 14))
    zeitlabel.pack(pady=10)

    def klick():
        punktzahl.set(punktzahl.get() + 1)

    klickbutton = tk.Button(fenster, text='Klickerhero', command=klick, font=('Gothic', 14), state='disabled')
    klickbutton.pack(pady=10)

    def countdown():
        if zeit.get() > 0:
            zeit.set(zeit.get() - 1)
            zeitlabel.config(text=F'Zeit: {zeit.get()} Sekunden')
            fenster.after(1000, countdown) #1sekunde ist 1000ms 
        else:
            klickbutton.config(state='disabled')
            zeitlabel.config(text=F'Over! Heroclicks: {punktzahl.get()}')
    
    def start_spiel():
        punktzahl.set(0)
        zeit.set(10)
        zeitlabel.config(text=F'Zeit: {zeit.get()} Sekunden')
        klickbutton.config(state='normal')
        countdown()

    
    restart_button = tk.Button(fenster, text='Ready?', command=start_spiel, font=('Gothic', 20))
    restart_button.pack(pady=20)
