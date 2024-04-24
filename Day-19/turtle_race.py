import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)

input_color = turtle.textinput('color', "What will be the color of winner turtle? ")
tims = [Turtle(shape="turtle") for i in range(6)]
colors = ["violet", "blue", "green", "yellow", "orange", "red"]
y_init = -100

for _ in range(6):
    tims[_].color(colors[_])
    tims[_].penup()
    tims[_].goto(x=-230, y=y_init)
    y_init += 40


completed = False
winner = None

while not completed:
    for tim in tims:
        tim.forward(random.randint(1, 10))
        if tim.pos()[0] >= 250:
            winner = tim.color()[0]
            completed = True


if input_color.lower() == winner:
    print(f"Winner is {winner}. You won.")
else:
    print(f"Winner is {winner}. You loose")
screen.exitonclick()
