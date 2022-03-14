from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.place()
        

    def place(self):
        r_x = random.randint(-280, 280)
        r_y = random.randint(-280, 280)
        self.setposition(r_x, r_y)