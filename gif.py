import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

def gifwindow():
    fenster = tk.Toplevel()
    fenster.title('GIF Fenster')
    fenster.geometry('400x400')

    # GIF-Bild laden
    gif = Image.open('dance.gif')  # Pfad zum GIF-Bild anpassen

    label = tk.Label(fenster)
    label.pack(expand=True)

    #alle frames vorbereiten
    frames = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(gif)]

    def animate(counter):
        # Nächsten Frame des GIFs anzeigen
        frame = frames[counter]
        label.config(image=frame)
        label.image = frame
        counter = (counter + 1) % gif.n_frames
        fenster.after(100, lambda: animate(counter))
    animate(0)  # Animation starten