import turtle as t
import colorgram as colorg
import random
import os

dir = os.path.dirname(os.path.realpath(__file__))
IMAGE = os.path.join(dir, 'hirst.jpg')
colors = colorg.extract(IMAGE, 35)

rgb_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_list.append((r, g, b))


t.colormode(255)
bill = t.Turtle()
bill.shape("turtle")
bill.color("DarkSlateBlue")
bill.pensize(20)
bill.speed(8)
bill.pu()
bill.hideturtle()
bill.setposition(-250, -200)

for _ in range(10):
    for _ in range(10):
        bill.dot(20, random.choice(rgb_list))
        bill.fd(50)
    bill.setposition(bill.xcor() - 500, bill.ycor() + 50)

screen = t.Screen()
screen.exitonclick()