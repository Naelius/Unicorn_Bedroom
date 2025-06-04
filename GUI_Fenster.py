import tkinter as tk
from buttonsaktion import button_action, gif_button, spiel_button
from buttonsaktion import button1_action, button2_action, button3_action, button4_action

from menue import add_menue

def create_mainwindow():
    #hauptfenster machen 

    root = tk.Tk()
    add_menue(root)  # Menüleiste hinzufügen
    root.title('Button Anwendung')
    root.geometry('600x600')
    root.configure(bg='lightgray')




#bruachte liste für die farben 
    farben = ['red', 'green', 'blue', 'orange', 'purple', 'cyan']


#lambda funktion einfach als fake funktion 
    funktionen = [ lambda: button1_action(status_label),  button2_action, button3_action, button4_action, spiel_button, gif_button]



#irgendwie ne for schleife herstellen um buttons zu erstellen
    for i, (farbe, funktion) in enumerate(zip(farben, funktionen)):
    
        button = tk.Button(
            root, text=F'Button {i+1}', bg=farbe, fg='white', command=funktion, font=('Gothic', 12), 
            width=15, height=2
        )
        button.pack(padx=5, pady=5, side='left')

    return root
