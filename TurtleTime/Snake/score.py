from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 14, "bold")
HSFONT = ("Courier", 12, "bold")
FILE = "data.txt"

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.pencolor("white")
        self.score = 0
        with open(FILE) as f:
            self.highscore = int(f.read())
        self.ht()
        self.pu()
        self.setposition(0, 270)
        self.write(self.score, move=False, align=ALIGN, font=FONT)

    def score_inc(self):
        self.clear()
        self.score += 1
        self.write(self.score, move=False, align=ALIGN, font=FONT)

    def game_over(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(FILE, mode="w") as f:
                f.write(str(self.score))
        self.setposition(0,0)
        self.write("GAME OVER", move=False, align=ALIGN, font=FONT)
        self.setposition(0, -20)
        self.write(f"High Score: {self.highscore}", align=ALIGN, font=HSFONT)

