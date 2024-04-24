import turtle as t
import random
from turtle_colors import colors


tim = t.Turtle()
t.colormode(255)
tim.width(8)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


screen = t.Screen()
screen.bgcolor(random_color())

directions = [0, 90, 180, 270]

for _ in range(500):
    tim.forward(20)
    tim.setheading(random.choice(directions))
    tim.color(random_color())
