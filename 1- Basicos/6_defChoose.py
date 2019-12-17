# -*- coding: utf-8 -*-
import turtle


def main():
    window = turtle.Screen()
    alan = turtle.Turtle()

    opcion = input('Elija la figura: Cuadrado (C) o Triangulo (T): ')

    if opcion.upper() == 'T':
        make_triangle(alan)
        turtle.mainloop()
    elif opcion.upper() == 'C':
        make_square(alan)
        turtle.mainloop()
    else:
        print('Figura elegida incorrecta')


def make_square(alan):
    length = int(input('Tamaño de cuadrado: '))

    for i in range(4):
        angle_square = 90
        make_line_and_turn(alan, length, angle_square)


def make_triangle(alan):
    length = int(input('Tamaño de triangulo: '))

    for i in range(3):
        '''
        if i == 1:
           angle_triangle = 120
        elif i == 2:
            angle_triangle = 120
        else:
            angle_triangle = 120
        '''
        angle_triangle = 120

        make_line_and_turn(alan, length, angle_triangle)


def make_line_and_turn(alan, length, angle):
    alan.forward(length)
    alan.left(angle)


if __name__ == '__main__':
    main()
