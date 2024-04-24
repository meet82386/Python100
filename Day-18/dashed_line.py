from turtle import Screen, Turtle

tim = Turtle()

for i in range(4):
    for _ in range(10):
        tim.forward(10)
        tim.penup()
        tim.forward(5)
        tim.pendown()
    tim.left(90)


screen = Screen()
screen.exitonclick()
