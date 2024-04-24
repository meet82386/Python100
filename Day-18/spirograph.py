import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
t.speed("fastest")


def get_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


angle = 0
while angle <= 360:
    t.color(get_color())
    t.circle(100)
    angle += 5
    t.setheading(angle)


screen = t.Screen()
screen.exitonclick()
