import random
from tkinter import *
from level.second_level import second_level
def first_level(root, canvas, square, signe_x, signe_y, vitesse):
    target_x = random.randint(10, 500)
    target_y = random.randint(5, 300)
    target = canvas.create_rectangle(target_x, target_y, target_x + 100, target_y + 100, fill="blue")

    while True:
        canvas.move(square, vitesse * signe_x[0], vitesse * signe_y[0])
        canvas.update()
        if canvas.coords(square)[2] >= 900 or canvas.coords(square)[0] <= 0:
            signe_x[0] *= -1
        if canvas.coords(square)[3] >= 800 or canvas.coords(square)[1] <= 0:
            signe_y[0] *= -1
        if (canvas.coords(square)[0] <= target_x + 10 and canvas.coords(square)[2] >= target_x + 90) and (canvas.coords(square)[1] <= target_y + 10 and canvas.coords(square)[3] >= target_y + 90):
            print("Level completed!")
            canvas.delete(target)
            second_level(root, canvas, square, signe_x, signe_y, vitesse)
        canvas.after(1)
        canvas.update()













