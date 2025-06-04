from PIL import Image, ImageTk
import tkinter as tk

class AnimatedGIF(tk.Label):
    def __init__(self, master, gif_path):
        im = Image.open(gif_path)
        seq = []
        try:
            while True:
                seq.append(im.copy())
                im.seek(len(seq))
        except EOFError:
            pass

        self.frames = [ImageTk.PhotoImage(img) for img in seq]
        self.frame_count = len(self.frames)
        self.delay = im.info.get('duration', 100)

        super().__init__(master, image=self.frames[0])
        self.idx = 0
        self.animate()

    def animate(self):
        self.config(image=self.frames[self.idx])
        self.idx = (self.idx + 1) % self.frame_count
        self.after(self.delay, self.animate)