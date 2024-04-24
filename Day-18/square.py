from turtle import Turtle, Screen

tim = Turtle(shape="turtle")

tim.forward(100)
for _ in range(3):
    tim.left(90)
    tim.forward(100)

tim.left(90)

screen = Screen()
screen.exitonclick()
