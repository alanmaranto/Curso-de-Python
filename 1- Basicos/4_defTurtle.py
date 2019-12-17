# -*- coding: utf-8 -*-

import turtle


def main():
    # Abriendo la ventana
    window = turtle.Screen()
    # Generar la tortuga
    alan = turtle.Turtle()

    make_square(alan)

    #evita que se cierre
    turtle.mainloop()


def make_square(alan):
    # se ejecute cuando doy enter asignado a una variable
    length = int(input('Tamaño de cuadrado: '))

    for i in range(4):
        make_line_and_turn(alan, 100)


def make_line_and_turn(alan, length):
    alan.forward(length)
    alan.left(90)


# Definiendo una expresion para que python no ejecute otros archivos
if __name__ == '__main__':
    main()
