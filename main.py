from turtle import Turtle ,Screen
from paddles import Paddle
from ball import  Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PONG")
screen.tracer(0)

scoreboard= ScoreBoard()


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.goup,"Up")
screen.onkey(r_paddle.godown,"Down")
screen.onkey(l_paddle.goup,"w")
screen.onkey(l_paddle.godown,"s")


game_is_on= True
while game_is_on:
    time.sleep(0.05)
    ball.ball_move()
    screen.update()

    if ball.ycor() >280 or ball.ycor()<-280:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() <340:
        ball.paddle_bounce()
        ball.ball_sped()

    if  ball.xcor() >380:
        ball.out_of_bounds()
        scoreboard.l_point()

    if  ball.xcor() < -380:
        ball.out_of_bounds()
        scoreboard.r_point()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.paddle_bounce()
        ball.ball_sped()


screen.exitonclick()