from tkinter import *
from user import input
from level import level

root = Tk()
root.title("Game Python")
root.geometry("900x800")
canvas = Canvas(root, width=900, height=800)
canvas.pack()

signe_x = [1]
signe_y = [1]
vitesse = 2  # Augmentez cette valeur pour augmenter la vitesse

square = canvas.create_rectangle(100, 100, 200, 200, fill="red")

input.bind_reverse_key(root, canvas, square, signe_x, signe_y)

level.second_level(root, canvas, square, signe_x, signe_y, vitesse)

root.mainloop()