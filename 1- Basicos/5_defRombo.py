# -*- coding: utf-8 -*-
import turtle


def main():
    window = turtle.Screen()
    alan = turtle.Turtle()

    make_diamond(alan)

    turtle.mainloop()


def make_diamond(alan):
    length = int(input('Tamaño del rombo: '))

    alan.left(45)
    alan.forward(length)

    for i in range(3):
        turn_and_make_line(alan, length)


def turn_and_make_line(alan, length):
    alan.left(90)
    alan.forward(length)


if __name__ == "__main__":
    main()
