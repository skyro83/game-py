from tkinter import *
from level.third_level import level_3
def second_level(root, canvas, square, signe_x, signe_y, vitesse):
    v_block2 = 5
    v = 5
    y_milieu = (canvas.coords(square)[1] + canvas.coords(square)[3]) / 2
    block1 = canvas.create_rectangle(50, y_milieu - 100, 25, y_milieu + 100, fill="black")
    block2 = canvas.create_rectangle(850, y_milieu - 100, 875, y_milieu + 100, fill="black")

    canvas.update()
    existe = False
    Existe = False

    while True:
        if canvas.coords(block1)[1] + vitesse * signe_y[0] < 0:
            if not Existe:
                N = canvas.create_rectangle(50, -100, 25, 200, fill="black")
                Existe = True
        elif Existe:
            canvas.delete(N)
            Existe = False

        elif canvas.coords(block1)[3] + vitesse * signe_y[0] > 800:
            if not existe:
                n = canvas.create_rectangle(50, 600, 25, 800, fill="black")
                existe = True
        else:
            if existe:
                canvas.delete(n)
                existe = False

        canvas.move(square, vitesse * signe_x[0], vitesse * signe_y[0])
        canvas.move(block1, 0, vitesse * signe_y[0])
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

        # Si le cube touche block2 sur les côtés haut et bas, il rebondit
        square_coords = canvas.coords(square)
        block2_coords = canvas.coords(block2)
        if (square_coords[2] >= block2_coords[0] and square_coords[0] <= block2_coords[2]):
            if (square_coords[3] >= block2_coords[1] and square_coords[1] <= block2_coords[1]):
                signe_y[0] *= -1
            elif (square_coords[1] <= block2_coords[3] and square_coords[3] >= block2_coords[3]):
                signe_y[0] *= -1

        # Si le cube touche block2 sur les côtés gauche et droit, il rebondit
        if (square_coords[2] >= block2_coords[0] and square_coords[0] <= block2_coords[2]) and (square_coords[3] >= block2_coords[1] and square_coords[1] <= block2_coords[3]):
            signe_x[0] *= -1

        # Vérifier si le cube touche la bordure droite
        if square_coords[2] >= 900:
            # Passer au niveau 3 (ou effectuer toute autre action nécessaire)
            level_3(root, canvas, square, signe_x, signe_y, v)

        canvas.after(1)
        canvas.update()