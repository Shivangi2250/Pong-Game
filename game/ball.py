from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move=10
        self.y_move=10
        self.move_speed=0.1

    def ball_move(self):
        # self.goto(x=380,y=283)  #my method of moving the ball to the top right corner
        # but not applicable for all the conditions
        new_x=self.xcor()+self.x_move  #from here is angela"s method which is all correct
        new_y=self.ycor() +self.y_move
        self.goto(new_x,new_y)

    def bounce(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move*=-1
        self.move_speed*=0.1

    def reset_position(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.bounce_x()









