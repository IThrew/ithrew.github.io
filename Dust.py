import tkinter as tk
import random
import time

class DustGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Dust Particle Collector")
        self.root.configure(bg="black")

        self.canvas = tk.Canvas(root, width=600, height=400, bg="black", highlightthickness=0)
        self.canvas.pack()

        self.label = tk.Label(root, text="Dust Collected: 0", fg="white", bg="black", font=("Courier", 16))
        self.label.pack()

        self.counter = 0
        self.dust = None
        self.moving = False

        self.spawn_dust()

    def spawn_dust(self):
        if self.dust:
            self.canvas.delete(self.dust)

        x = random.randint(50, 550)
        y = random.randint(50, 350)
        self.dust = self.canvas.create_oval(x, y, x+10, y+10, fill="gray")
        self.canvas.tag_bind(self.dust, "<Button-1>", self.collect_dust)

        if not self.moving:
            self.move_dust()

    def move_dust(self):
        if not self.dust:
            return
        self.canvas.move(self.dust, 1, 0)  # 1 pixel per second
        self.root.after(1000, self.move_dust)

    def collect_dust(self, event):
        self.counter += 1
        self.label.config(text=f"Dust Collected: {self.counter}")
        self.canvas.delete(self.dust)
        self.dust = None
        self.root.after(1 * 60 * 1000, self.spawn_dust)  # 1 minute delay

root = tk.Tk()
game = DustGame(root)
root.mainloop()
