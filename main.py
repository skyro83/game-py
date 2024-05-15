from tkinter import *
from user import input

root = Tk()
root.title("Game Python")
root.geometry("600x400")
canvas = Canvas(root, width=600, height=400)
canvas.pack()

signe_x = [1]
signe_y = [1]
vitesse = 2  # Augmentez cette valeur pour augmenter la vitesse

square = canvas.create_rectangle(100, 100, 200, 200, fill="red")

input.bind_reverse_key(root, canvas, square, signe_x, signe_y)

while True:
    canvas.move(square, vitesse * signe_x[0], vitesse * signe_y[0])
    canvas.update()
    if canvas.coords(square)[2] >= 600 or canvas.coords(square)[0] <= 0:
        signe_x[0] *= -1
    if canvas.coords(square)[3] >= 400 or canvas.coords(square)[1] <= 0:
        signe_y[0] *= -1
    canvas.after(1)
    canvas.update()

root.mainloop()