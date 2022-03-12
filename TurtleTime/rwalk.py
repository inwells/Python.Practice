import turtle as t
import random as rad

t.colormode(255)
bill = t.Turtle()
bill.shape("turtle")
bill.color("DarkSlateBlue")
bill.pensize(10)
bill.speed(0)
directions = [0, 90, 180, 270]

def random_color():
    r = rad.randint(0, 255)
    g = rad.randint(0, 255)
    b = rad.randint(0, 255)
    color = (r, g, b)
    return color

for _ in range(150):
    bill.pencolor(random_color())
    bill.right(rad.choice(directions))
    bill.fd(rad.randint(5, 100))

screen = t.Screen()
screen.exitonclick()