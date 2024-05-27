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

def level_3(root, canvas, square, signe_x, signe_y, vitesse):
    # Repositionner le cube à gauche de l'écran
    canvas.coords(square, 50, 400, 75, 425)

    # Créer le labyrinthe (exemple de labyrinthe simple)
    walls = [
        (100, 0, 125, 300),
        (200, 200, 225, 600),
        (300, 0, 325, 400),
        (400, 300, 425, 700),
        (500, 0, 525, 500),
        (600, 400, 625, 800),
        (700, 100, 725, 600),
        (800, 300, 825, 800)
    ]

    for wall in walls:
        canvas.create_rectangle(wall, fill="black")

    # Position de la sortie
    exit_position = (850, 400, 875, 425)
    canvas.create_rectangle(exit_position, fill="green")

    # Boucle de déplacement du cube
    while True:
        # Déplacer le cube
        canvas.move(square, vitesse * signe_x[0], vitesse * signe_y[0])
        square_coords = canvas.coords(square)

        # Vérifier les collisions avec les murs
        for wall in walls:
            if intersects(square_coords, wall):
                # Récupérer les coordonnées des côtés du mur
                wall_left, wall_top, wall_right, wall_bottom = wall
                square_left, square_top, square_right, square_bottom = square_coords
                
                # Calculer les distances entre les côtés du cube et les côtés du mur
                dx_left = abs(square_right - wall_left)
                dx_right = abs(square_left - wall_right)
                dy_top = abs(square_bottom - wall_top)
                dy_bottom = abs(square_top - wall_bottom)
                
                # Déterminer la distance minimale
                min_dx = min(dx_left, dx_right)
                min_dy = min(dy_top, dy_bottom)
                
                # Si la collision est sur l'axe horizontal, inverser signe_x
                if min_dx < min_dy:
                    signe_x[0] *= -1
                # Sinon, inverser signe_y
                else:
                    signe_y[0] *= -1
                
                break

        # Vérifier les collisions avec les bords du canvas
        # Note: La vérification de la bordure droite a été commentée pour ignorer la condition de changement de niveau
        if square_coords[2] >= 900 or square_coords[0] <= 0:
            signe_x[0] *= -1
        if square_coords[3] >= 800 or square_coords[1] <= 0:
            signe_y[0] *= -1

        # Vérifier si le cube touche le bloc vert avec une marge d'erreur
        if (square_coords[2] >= exit_position[0] - 5 and square_coords[0] <= exit_position[2] + 5) and (square_coords[3] >= exit_position[1] - 5 and square_coords[1] <= exit_position[3] + 5):
            print("Fini")
            root.destroy()  # Fermer la fenêtre
            return

        canvas.after(10)
        canvas.update()

def intersects(rect1, rect2):
    """Vérifie si deux rectangles s'intersectent"""
    x1, y1, x2, y2 = rect1
    x3, y3, x4, y4 = rect2
    return not (x2 < x3 or x1 > x4 or y2 < y3 or y1 > y4)













