import random
from tkinter import *

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


def second_level(root, canvas, square, signe_x, signe_y, vitesse):
    v_block2 = 2
    y_milieu=(canvas.coords(square)[1]+canvas.coords(square)[3])/2
    block1 = canvas.create_rectangle(50, y_milieu -100, 25, y_milieu+100, fill="black")
    block2 = canvas.create_rectangle(850, y_milieu - 100, 875, y_milieu + 100, fill="black")

    canvas.update()
    existe=False
    Existe=False
    while True:

        if canvas.coords(block1)[1] + vitesse * signe_y[0]<0:
            if not(Existe):
                N=canvas.create_rectangle(50, -100, 25, 200, fill="black")
                Existe=True
        elif Existe:
                canvas.delete(N)
                Existe = False

        elif canvas.coords(block1)[3] + vitesse * signe_y[0]>800:
            if not(existe):
                n=canvas.create_rectangle(50, 600, 25, 800, fill="black")
                existe=True
        else:
            if existe:
                canvas.delete(n)
                existe = False
        
        canvas.move(square, vitesse * signe_x[0], vitesse * signe_y[0])
        

        canvas.move(block1, 0, vitesse * signe_y[0]  )

        canvas.move(block2, 0, v_block2)  
        # Si le bloc 2 atteint le bord du canvas, il part dans l'autre sens
        if canvas.coords(block2)[3] >= 800 or canvas.coords(block2)[1] <= 0:
            v_block2 *= -1
        
        canvas.update()
        if canvas.coords(square)[2] >= 900 or canvas.coords(square)[0] <= 0:
            signe_x[0] *= -1
        if canvas.coords(square)[3] >= 800 or canvas.coords(square)[1] <= 0:
            signe_y[0] *= -1

        if canvas.coords(square)[0] <= 50:
            signe_x[0] *= -1
        
        # Si le cube touche block2, il rebondit
        if (canvas.coords(square)[2] >= canvas.coords(block2)[0] and canvas.coords(square)[0] <= canvas.coords(block2)[2]) and (canvas.coords(square)[3] >= canvas.coords(block2)[1] and canvas.coords(square)[1] <= canvas.coords(block2)[3]):
            signe_x[0] *= -1
        
        canvas.after(1)
        canvas.update()