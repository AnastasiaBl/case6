'''Developers:
Andrew Manko,Anastasia Bliznyak'''
import ru_local
import turtle
from math import *

print('{:^50s}'.format(ru_local.RED))
print('{:^50s}'.format(ru_local.ORANGE))
print('{:^50s}'.format(ru_local.YELLOW))
print('{:^50s}'.format(ru_local.GREEN))
print('{:^50s}'.format(ru_local.BLUE))
print('{:^50s}'.format(ru_local.PURPLE))




def get_color_choice():
    """Функция для выбора цвета заливки шестиугольника"""
    a = str(input(ru_local.COLOR_1))
    a = a.lower()
    while True:
        if a == ru_local.RED1 or ru_local.ORANGE1 or a == ru_local.YELLOW1 or a == ru_local.GREEN1 or a == ru_local.BLUE1 or a == ru_local.PURPLE1:
            color1 = a
            if color1 == ru_local.RED1:
                color1 = 'red'
                break
            elif color1 == ru_local.ORANGE1:
                color1 = 'orange'
                break
            elif color1 == ru_local.YELLOW1:
                color1 = 'yellow'
                break
            elif color1 == ru_local.GREEN1:
                color1 = 'green'
                break
            elif color1 == ru_local.BLUE1:
                color1 = 'blue'
                break
            elif color1 == ru_local.PURPLE1:
                color1 = 'purple'
                break
        else:
            print(ru_local.ERROR)
            a = str(input(ru_local.COLOR_1))
            a = a.lower()
            continue
    return color1


def get_color_choice1():
    """Функция для выбора цвета заливки шестиугольника"""
    b = str(input(ru_local.COLOR_2))
    b = b.lower()
    while True:
        if b == ru_local.RED1 or b == ru_local.ORANGE1 or b == ru_local.YELLOW1 or b == ru_local.GREEN1 or b == ru_local.BLUE1 or b == ru_local.PURPLE1:
            color2 = b
            if color2 == ru_local.RED1:
                color2 = 'red'
                break
            elif color2 == ru_local.ORANGE1:
                color2 = 'orange'
                break
            elif color2 == ru_local.YELLOW1:
                color2 = 'yellow'
                break
            elif color2 == ru_local.GREEN1:
                color2 = 'green'
                break
            elif color2 == ru_local.BLUE1:
                color2 = 'blue'
                break
            elif color2 == ru_local.PURPLE1:
                color2 = 'purple'
                break
        else:
            print(ru_local.ERROR)
            b = str(input(ru_local.COLOR_2))
            b = b.lower()
            continue
    return color2


def get_num_hexagons():
    """Функция для ввода количества шестиугольников"""
    i = int(input(ru_local.COUNT))
    while True:
        if i > 3 and i < 21:
            try:
                i = int(i)
                return i
            except ValueError:
                print(ru_local.ERROR1)
        else:
            i = str(input(ru_local.ERROR1))
            continue
    return i


def draw_hexagon(side_len):
    """Функция рисования шестиугольника"""
    s = 0
    turtle.begin_fill()
    turtle.right(30)
    while s != 600:
        turtle.fd(side_len)
        turtle.right(60)
        s += 120
    turtle.fd(side_len)
    turtle.right(30)
    turtle.end_fill()


color1 = get_color_choice()
color2 = get_color_choice1()
i = get_num_hexagons()

side_len = float(sqrt(4 * (500 / (2 * i)) ** 2 / 3))

size = (500, 500)
y = 250
x = -250
line = 1
hexagon = 1

for hexagons in range(i):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()

    if line % 2 == 1:

        for hexagons in range(i):

            if hexagon % 2 == 1:
                turtle.fillcolor(color1)
                draw_hexagon(side_len)
                turtle.up()
                turtle.fd(sqrt(side_len ** 2 - (side_len / 2) ** 2) * 2)
                turtle.down()
                hexagon += 1

            else:
                turtle.fillcolor(color2)
                draw_hexagon(side_len)
                turtle.up()
                turtle.fd(sqrt(side_len ** 2 - (side_len / 2) ** 2) * 2)
                turtle.down()
                hexagon += 1

        turtle.up()
        y = y - 3 * side_len / 2
        x = x - sqrt(side_len ** 2 - (side_len / 2) ** 2)
        turtle.goto(x, y)
        turtle.down()
        line += 1

    else:

        for hexagons in range(i):

            if hexagon % 2 == 1:
                turtle.fillcolor(color2)
                draw_hexagon(side_len)
                turtle.up()
                turtle.fd(sqrt(side_len ** 2 - (side_len / 2) ** 2) * 2)
                turtle.down()
                hexagon += 1

            else:
                turtle.fillcolor(color1)
                draw_hexagon(side_len)
                turtle.up()
                turtle.fd(sqrt(side_len ** 2 - (side_len / 2) ** 2) * 2)
                turtle.down()
                hexagon += 1

        turtle.up()
        y = y - 3 * side_len / 2
        x = x + sqrt(side_len ** 2 - (side_len / 2) ** 2)
        turtle.goto(x, y)
        turtle.down()
        line += 1
        hexagon += 1
turtle.done()



