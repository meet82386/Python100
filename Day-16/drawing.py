from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")

my_screen = Screen()
print(my_screen.canvheight)

i = 0
while i < 1000:
    timmy.forward(150)
    timmy.left(45)
    timmy.forward(150)
    timmy.left(45)
    timmy.backward(150)
    if i % 4 == 0:
        timmy.right(100)
    if i % 60 == 0:
        timmy.left(170)
        timmy.circle(25.0)

my_screen.exitonclick()
