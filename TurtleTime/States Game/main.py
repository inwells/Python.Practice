import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

t = turtle.Turtle()
t.hideturtle()
t.penup()

answered_states = []
states = pd.read_csv("50_states.csv")
all_states = states.state.to_list()

print(states)

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()


while all_states != answered_states:
    answer = screen.textinput(title="Guess the State", prompt="Name a state?")
    if answer in all_states and answer not in answered_states:
        st_data = states[states.state == answer]
        t.goto(int(st_data.x), int(st_data.y))
        t.write(answer)
        answered_states.append(answer)

screen.exitonclick()