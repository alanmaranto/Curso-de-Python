# -*- coding: utf-8 -*-
import turtle

def main():
    window = turtle.Screen()
    star = turtle.Turtle()

    make_star(star)

    turtle.mainloop()

def make_star(star):
    length = int(input('Digite el tamaño de la estrella:'))

    for i in range(9):
        make_line_and_turn(star, length)

def make_line_and_turn(star, length):
    star.forward(length)
    star.right(200)

if __name__ == '__main__':
    main()