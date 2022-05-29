from turtle import Turtle 
STARTSCORE=0
XCOR1=-50
XCOR2=50
YCOR = 250 
STYLE = ("Courier" , 20 , "bold")
class Score(Turtle):
    def __init__(self) :
        super().__init__() 
        self.penup() 
        self.hideturtle()
        self.goto(-0,270) 
        self.color("white")
    def board(self,score1,score2):
        self.clear()
        self.write(f"PLAYER ONE : {score1} VS PLAYER TWO : {score2}", font=STYLE, align="center")    
        


