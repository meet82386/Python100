from turtle import Turtle, Screen
import random
from turtle_colors import colors

tim = Turtle()
tim.width(2)

for i in range(3, 11):
    angle = 360 / i
    tim.color(random.choice(colors))
    for j in range(0, i):
        tim.forward(100)
        tim.right(angle)

for i in range(3, 11):
    angle = 360 / i
    tim.color(random.choice(colors))
    for j in range(0, i):
        tim.forward(100)
        tim.left(angle)

screen = Screen()
screen.exitonclick()
