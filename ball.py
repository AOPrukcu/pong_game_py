from turtle import  Turtle
import random
degrees =[0,30,60,120,150,210,240,270]
wall=(-300,300)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.degree = random.choice(degrees)
        self.goto(0,0)
        self.x_move=10
        self.y_move= 10

        self.speed("slowest")


    def ball_move(self):
        new_x= self.xcor() + self.x_move
        new_y= self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.bounce()
        self.x_move *= -1

    def out_of_bounds(self):
        self.goto(0,0)
        self.x_move=10
        self.y_move= 10



    def ball_sped(self):
        if self.x_move <0:
            self.x_move -=5
        else:
            self.x_move +=5
