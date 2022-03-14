from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 14, "bold")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.pencolor("white")
        self.score = 0
        self.ht()
        self.pu()
        self.setposition(0, 270)
        self.write(self.score, move=False, align=ALIGN, font=FONT)

    def score_inc(self):
        self.clear()
        self.score += 1
        self.write(self.score, move=False, align=ALIGN, font=FONT)

    def game_over(self):
        self.setposition(0,0)
        self.write("GAME OVER", move=False, align=ALIGN, font=FONT)

