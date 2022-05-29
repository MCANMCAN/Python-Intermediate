from turtle import Turtle 
import random 

class Ball(Turtle):
    def __init__(self) :
        super().__init__() 
        self.color("white")
        self.shape("circle")
        self.shapesize(1)
        self.angles = [15,30,45,315,330,345,135]
        self.penup()
        self.first_move()
    def first_move(self): 
        self.hideturtle()
        self.goto(0,0)
        self.showturtle()
        first_angle = random.choice(self.angles)
        #first_angle = 290
        self.setheading(first_angle)
    
        