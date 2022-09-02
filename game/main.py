from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score

screen = Screen()
screen.listen()
screen.setup(width=800, height=600)
screen.bgcolor("green")
screen.title("WELCOME TO THE PONG GAME 😎")
screen.tracer()

dotted_line = Turtle()
dotted_line.hideturtle()
dotted_line.color("white")

dotted_line.speed("fastest")
dotted_line.penup()
dotted_line.sety(320)
dotted_line.shape("arrow")
dotted_line.pensize(5)
dotted_line.setheading(270)

for i in range(25):
    if i % 2 == 0:
        dotted_line.penup()
        dotted_line.forward(30)

    else:
        dotted_line.pendown()
        dotted_line.forward(30)


l_paddle = Paddle(-350)
r_paddle=Paddle(350)
ball=Ball()
scoreboard=Score()



screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")




game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()
    #detect collision with wall and bounce
    if ball.ycor()>280 or ball.ycor()<-275:
        ball.bounce()
    #detect collision with wall and bounce
    if ball.distance(r_paddle)<50 and ball.xcor()>330 or ball.distance(l_paddle)<50 and ball.xcor()<-330:
        ball.bounce_x()



    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()





screen.exitonclick()
