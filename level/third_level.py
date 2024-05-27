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