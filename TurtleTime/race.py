import turtle as t
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
ya=-100
for i in range(6):
    name = colors[i]
    name = t.Turtle(shape="turtle")
    name.color(colors[i])
    name.speed(random.randint(0, 10))
    name.pu()
    ya += 30
    name.goto(x=-230, y=ya)
    turtles.append(name)


screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bet", prompt="What color do you think will win?")

if user_bet:
    race = True

while race:
    for turtle in turtles:
        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if winner == user_bet:
                print("You won!")
            else:
                print("You lost!")
            race = False
screen.exitonclick()
