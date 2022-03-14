from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed(3)
        #self.shapesize(stretch_wid=5, stretch_len=1)
        self.pu()
        self.speed = .1
        self.setheading(150)

    def move(self):
        self.fd(self.speed)

    def bounce(self, surface):
        if surface == "wall":
            self.setheading(360 - self.heading())
        elif surface == "paddle":
            if self.heading() < 180:
                print("bounce up")
                self.setheading(180 - self.heading())
            else:
                self.setheading((180 - self.heading()) + 360)
                print("down")
    
    def reset_pos(self):
        self.setposition(0, 0)
        self.bounce("paddle")
