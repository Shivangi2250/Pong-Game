from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x):
        super().__init__()
        self.penup()
        self.speed(10)
        self.setx(x)
        # self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1,outline=None)

    def up(self):
        self.speed('fastest')
        self.sety(self.ycor() + 50)

    def down(self):
        self.speed('fastest')
        self.sety(self.ycor() - 50)








