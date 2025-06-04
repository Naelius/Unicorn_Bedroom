import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

class AnimationWindow(tk.Toplevel):
    """
    Klasse für das Animationsfenster.
    Diese Klasse erbt von `tk.Toplevel` und implementiert eine Animation,
    die aus einem GIF-Bild besteht. Die Animation wird in einem Canvas angezeigt.
    """
    def __init__(self, master):
        """
        Initialisiert das Animationsfenster.
        :param master: Das Hauptfenster, von dem dieses Fenster abgeleitet wird.
        """
        super().__init__(master)
        self.title("Animation")
        
        gif = Image.open("assets/animation.gif")
        self.width, self.height = gif.size
        self.canvas = tk.Canvas(self, width=self.width, height=self.height)
        self.canvas.pack()

        self.frames = [
            ImageTk.PhotoImage(frame.copy().convert("RGBA"))
            for frame in ImageSequence.Iterator(gif)
        ]
        self.frame_index = 0
        self.animate()

    def animate(self):
        """
        Aktualisiert die Animation, indem das nächste Frame angezeigt wird.
        Diese Methode wird rekursiv aufgerufen, um die Animation fortzusetzen.
        """
        self.canvas.delete("all")
        self.canvas.create_image(self.width // 2, self.height // 2, image=self.frames[self.frame_index])
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.after(100, self.animate)
