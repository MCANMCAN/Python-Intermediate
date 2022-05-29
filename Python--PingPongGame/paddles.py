from turtle import Turtle

class Paddle(Turtle) :
    def __init__(self,ycor):
        super().__init__()
        self.start_position(ycor)
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.current_y = 0
        
    def start_position(self,xcor):
        self.goto(xcor,0)
        self.penup()
        self.current_x = xcor
    def up(self): 
        self.current_y = self.ycor() 
        self.current_y+=20
        self.goto( self.current_x,self.current_y) 
    def down(self): 
        self.current_y = self.ycor() 
        self.current_y-=20
        self.goto( self.current_x,self.current_y)
        
    
