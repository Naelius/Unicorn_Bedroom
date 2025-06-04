import tkinter as tk
from buttonsaktion import gif_button, spiel_button
from buttonsaktion import button1_action, button2_action, button3_action, button4_action

from menue import add_menue

def create_mainwindow():
    #hauptfenster machen 

    root = tk.Tk()
    add_menue(root)  # Menüleiste hinzufügen
    root.title('Button Anwendung')
    root.geometry('800x600')
    root.configure(bg='lightgray')

    #brauch ein label für meine knöpfe sonst geht nix
    status_label = tk.Label(root, text='ich bin BEREIT!', font=('Gothic', 20), bg='lightgray')
    status_label.pack(pady=10)

    #brauch ein label für den timer
    timer_label = tk.Label(root, text='Zeit: 0', font=('Gothic', 12), bg='lightgray')
    timer_label.pack(pady=10)


#bruachte liste für die farben 
    farben = ['red', 'green', 'blue', 'orange', 'purple', 'cyan']


#lambda funktion einfach als fake funktion 
    funktionen = [ lambda: button1_action(status_label),  button2_action, 
                  lambda: button3_action(status_label), 
                  lambda: button4_action(timer_label), 
                  spiel_button, 
                  gif_button
                  ]



#irgendwie ne for schleife herstellen um buttons zu erstellen
    for i, (farbe, funktion) in enumerate(zip(farben, funktionen)):
    
        button = tk.Button(
            root, text=F'Button {i+1}', bg=farbe, fg='white', command=funktion, font=('Gothic', 12), 
            width=15, height=2
        )
        button.pack(padx=5, pady=5, side='left')

    return root
