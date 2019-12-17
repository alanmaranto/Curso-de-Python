import turtle
def inicio():
    window = turtle.Screen()
    santi = turtle.Turtle()

    make_triangle(santi)


def make_triangle(santi):
    length = int(input("Ingresa la medida del triangulo: "))
    for i in range(3):

        make_line_and_turn(santi, length)


def make_line_and_turn(santi, length):
    santi.forward(length)
    santi.left(120)


if __name__ == "__main__":
    inicio()
    input()
