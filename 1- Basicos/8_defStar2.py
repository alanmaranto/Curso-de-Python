# -*- coding: utf-8 -*-
import turtle


def main():
    window = turtle.Screen()
    dave = turtle.Turtle()

    make_star(dave)

    turtle.mainloop()


def make_star(dave):
    tips = int(input('Número de puntas: '))
    length = int(input('Tamaño de la estrella: '))

    if tips % 2 == 0:
        angle = (tips//2+1)*360/tips
    else:
        angle = (tips//2)*360/tips

    for i in range(tips):
        make_line_and_turn(dave, length , angle)



def make_line_and_turn(dave, length, angle):
    dave.forward(length)
    dave.right(angle)


if __name__ == '__main__':
    main()