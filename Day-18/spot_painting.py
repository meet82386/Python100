import random
import turtle as t
import colorgram

tim = t.Turtle()
t.colormode(255)
t.speed("fastest")
colors = colorgram.extract('images.png', 10)
rgb_colors = list()


screen = t.Screen()
screen.setup(500, 500)


for _ in colors:
    r = _.rgb.r
    g = _.rgb.g
    b = _.rgb.b
    rgb_colors.append((r, g, b))

tim.penup()
x, y = -230, -230
tim.setpos(x, y)
tim.pendown()

while tim.pos()[1] < 250:
    while tim.pos()[0] < 250:
        print(tim.pos())
        tim.dot(20, random.choice(rgb_colors))
        tim.penup()
        tim.forward(50)
    y += 50
    tim.setpos(x, y)

screen.exitonclick()
