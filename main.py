from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard 
import time


ball_speed = 0
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("pong")
screen.tracer(0)

paddle_r = Paddle((360,0))
paddle_l = Paddle((-360,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_r.go_up,"Up")
screen.onkey(paddle_r.go_down,"Down")

screen.onkey(paddle_l.go_up,"w")
screen.onkey(paddle_l.go_down,"s")

gameis_on = True
while gameis_on:
    screen.update()
    ball.move()
    time.sleep(0.1 - ball_speed)

    if( ball.ycor()>280 or ball.ycor()<-280):
        ball.bounce_y()

    if( (ball.distance(paddle_r)<50 and ball.xcor()>340) or ball.distance(paddle_l)<30 and ball.xcor()>-370):
        ball.bounce_x()
        if(ball_speed < 0.069):ball_speed += 0.003

    if(ball.xcor() > 380 ):
        ball.reset_pos()
        ball_speed = 0
        scoreboard.l_point()

    if(ball.xcor() < -380 ):
        ball.reset_pos()
        ball_speed = 0
        scoreboard.r_point()
        
screen.exitonclick() 










