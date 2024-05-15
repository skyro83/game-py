def bind_reverse_key(root, canvas, square, signe_x, signe_y):
    def reverse_direction(event):
        signe_x[0] *= -1
        signe_y[0] *= -1

    root.bind('<KeyPress-+>', reverse_direction)