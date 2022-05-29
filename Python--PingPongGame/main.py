from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
import random
import time
from scoreboard import Score
ONE_X = -380
TWO_X = 380
screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")

paddle_one = Paddle(ONE_X)
paddle_two = Paddle(TWO_X)
sb=Score()
ball = Ball()
screen.listen()
screen.onkey(paddle_two.up,"Up")
screen.onkey(paddle_two.down,"Down")
screen.onkey(paddle_one.up,"w")
screen.onkey(paddle_one.down,"s")
game_on=True
in_game = True
scorex = 0 
scorey = 0 

while game_on == True : 
    #ball.first_move()
    #in_game == True
    
    sb.board(scorex,scorey)
    paddle_one.start_position(ONE_X)
    paddle_two.start_position(TWO_X)
    ball.first_move()
    time.sleep(1)
    ball.forward(20)
    in_game = True
    winner = Turtle()
    winner.penup()
    winner.hideturtle()
    winner.color("white")
    while in_game == True: 
        
        ball.forward(20)
        curang = ball.heading()
        #print(curang,type(curang))
        
        if ball.ycor() >= 290 and curang > 0 and curang < 90 : 
            curang = ball.heading()
            curang = 360-curang     
        elif ball.ycor() >= 290 and curang > 90 and curang < 180 : 
            curang = ball.heading()
            curang = 360 - curang  
        elif ball.ycor() <= -290 and curang > 180 and curang < 270 :
            curang = ball.heading()
            curang = 360 - curang
        elif ball.ycor() <= -290 and curang > 270 and curang < 360 :
            curang = ball.heading()
            curang = 360 - curang
        ball.setheading(curang)
        
        if paddle_one.distance(ball) < 20 : 
            curang = ball.heading()
            curang = random.randint(30,60)
        elif paddle_two.distance(ball) < 20 : 
            curang = ball.heading()
            curang = random.randint(200,230) 
        ball.setheading(curang)
             
        if ball.xcor() > 400 : 
            #print("pone scored")
            scorex += 1
            in_game = False
            
        elif ball.xcor() < -400 : 
            #print("ptwo scored")
            scorey += 1
            in_game = False
        #print(in_game)
    if scorex == 3 or scorey == 3 : 
        sb.board(scorex,scorey)
        if scorex == 3 : 
            winner.write("Player One won",align="center",font=("Courier" , 20 , "bold"))    
        elif scorey == 3 : 
            winner.write("Player Two won",align="center",font=("Courier" , 20 , "bold")) 
        game_on = False
    #print(game_on)
screen.exitonclick()