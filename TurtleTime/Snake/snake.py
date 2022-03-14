from pickletools import read_unicodestring1
import turtle as t
START_POS = [(0, 0),(-20, 0),(-40, 0)]
M_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        

    def create_snake(self):
        for pos in START_POS:
            self.add_seg(pos)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_seg(self, pos):
        new_seg = t.Turtle(shape="square")
        new_seg.color("white")
        new_seg.pu()
        new_seg.setposition(pos)
        self.segments.append(new_seg)

    def grow(self):
        self.add_seg(self.segments[-1].position())

    def move(self):
        for seg_numb in range(len(self.segments) - 1, 0, -1):
            m_x = self.segments[seg_numb - 1].xcor()
            m_y = self.segments[seg_numb - 1].ycor()
            self.segments[seg_numb].goto(m_x, m_y)
        self.head.fd(M_DIST)
