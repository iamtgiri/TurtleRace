from turtle import *
from random import *
import turtle
import time  
# from tkinter import *
# from tkinter import messagebox


# SCREEN SETUP 
screen = turtle.Screen()
screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)
title(":: The Turtle Race ::")



############### STAGE 1 ########################
bgcolor("black")
speed(0) 
name = textinput("Enter your name", "What is your name?")
penup()
goto(-400, 0)
color("yellow")
write(f"Hello {name}, Welcome to The Turtle Race", font=("Arial", 35))
time.sleep(3)

############### STAGE 2 ########################

bgcolor("forestgreen")
with open("scores.txt") as f:
    score = int(f.read())
while True:
    # Cover
    goto(-650, 350)
    color("forestgreen")
    begin_fill()
    for i in range(2):
        forward(1300)
        right(90)
        forward(700)
        right(90)
    end_fill()
    
    
    
    # HEADINGS 
    goto(-150,310)
    color("white")
    write("THE TURTLE RACE", font=("Arial", 30, "bold"))

    # PLAYER NAME
    goto(-550, 310)
    write(f"Player Name:{name}", font=("Arial", 15))

    # PLAYER SCORE 
    goto(420, 310)
    write(f"Points:{score}", font=("Arial", 15))

    # Playground
    # BOUNDARY 
    goto(-550, 300)
    width(4)
    color("white")
    pendown()
    for i in range(2):
        forward(1100)
        right(90)
        forward(600)
        right(90)
    penup()


    # DART
    goto(-550, 300)
    color("green")
    begin_fill()
    for i in range(2):
        forward(1100)
        right(90)
        forward(600)
        right(90)
    end_fill()

    # FINISH LINE 
    gap_size = 10
    shape("square")

    # WHITE SQUARE ROW 1
    color("white")
    for i in range(15):
        goto(450, (290 - i*gap_size*4))
        stamp()

    # WHITE SQUARE ROW 2
    for i in range(15):
        goto(450 + gap_size + 10, (290 - (2 + 4*i)*gap_size))
        stamp()

    # BLACK SQUARE ROW 1
    color("black")
    for i in range(15):
        goto(450,  (290 - (2 + 4*i)*gap_size))
        stamp()

    # Black SQUARE ROW 2
    for i in range(15):
        goto(450 + gap_size + 10, (290 - i*4*gap_size))
        stamp()


    ############ TURTLE DESIGN ###########  
    # TURTLE 1 - BLUE 
    blue_turtle = Turtle()
    blue_turtle.color("purple")
    blue_turtle.shape("turtle")
    blue_turtle.shapesize(2)
    blue_turtle.penup()
    blue_turtle.goto(-500, 250)
    blue_turtle.pendown()

    # TURTLE 2 - WHITE 
    pink_turtle = Turtle()
    pink_turtle.color("white")
    pink_turtle.shape("turtle")
    pink_turtle.shapesize(2)
    pink_turtle.penup()
    pink_turtle.goto(-500, 100)
    pink_turtle.pendown()

    # TURTLE 3 - YELLOW 
    yellow_turtle = Turtle()
    yellow_turtle.color("yellow")
    yellow_turtle.shape("turtle")
    yellow_turtle.shapesize(2)
    yellow_turtle.penup()
    yellow_turtle.goto(-500, -50)
    yellow_turtle.pendown()

    # TURTLE 4 - RED
    red_turtle = Turtle()
    red_turtle.color("red")
    red_turtle.shape("turtle")
    red_turtle.shapesize(2)
    red_turtle.penup()
    red_turtle.goto(-500, -200)
    red_turtle.pendown()

    ############ PROMPT SETUP ############
    bop = True
    while bop :
        bet_option = int(textinput(title = "Choose you Turtle", prompt="Which turtle will win the game? \n Choose a number between 1-4"))
        
        if bet_option == 1 or bet_option == 2 or bet_option == 3 or bet_option == 4:
            bop = False

    bam = True
    while bam:
        bet_amount = int(textinput(title="Enter Amount...", prompt=f"Points you have now : {score} \nHow much you want to use?"))

        if bet_amount <= score and bet_amount > 0:
            bam = False 
        

    # PAUSE 
    time.sleep(0.5)

    ############ MOVEMENT ############
    while blue_turtle.xcor() <= 418 and pink_turtle.xcor() <= 418 and yellow_turtle.xcor() <= 418 and red_turtle.xcor() <= 418:
        
        if blue_turtle.ycor() >= 275:
            blue_turtle.right(45)
            blue_turtle.forward(8)
        if blue_turtle.ycor() <= -275:
            blue_turtle.right(-45)
            blue_turtle.forward(8)
        if  blue_turtle.xcor() <= -505:
            blue_turtle.right(-135)
            blue_turtle.forward(8)
            
        blue_turtle.forward(randint(1,10))
        blue_turtle.right(randint(-10,10))
        
        if pink_turtle.ycor() >= 275:
            pink_turtle.right(90)
            pink_turtle.forward(8)
        if pink_turtle.ycor() <= -275:
            pink_turtle.right(-90)
            pink_turtle.forward(8)
        if  pink_turtle.xcor() <= -505:
            pink_turtle.right(-135)
            pink_turtle.forward(8)
        pink_turtle.forward(randint(1,10))
        pink_turtle.right(randint(-10,10))
        
        if yellow_turtle.ycor() >= 275:
            yellow_turtle.right(90)
            yellow_turtle.forward(8)
        if yellow_turtle.ycor() <= -275:
            yellow_turtle.right(-90)
            yellow_turtle.forward(8)
        if  yellow_turtle.xcor() <= -505:
            yellow_turtle.right(-135)
            yellow_turtle.forward(8)
        yellow_turtle.forward(randint(1,10))
        yellow_turtle.right(randint(-10,10))
        
        if red_turtle.ycor() >= 275:
            red_turtle.right(90)
            red_turtle.forward(8)
        if red_turtle.ycor() <= -275:
            red_turtle.right(-90)
            red_turtle.forward(8)
        if  red_turtle.xcor() <= -505:
            red_turtle.right(-135)
            red_turtle.forward(8)
        red_turtle.forward(randint(1,10))
        red_turtle.right(randint(-10,10))

    penup()
    blue_turtle.penup()
    pink_turtle.penup()
    yellow_turtle.penup()
    red_turtle.penup()

    ############# RESULT ############# 
    if blue_turtle.xcor() >= 418:
        for i in range(36):
            blue_turtle.right(10)
            blue_turtle.shapesize(3)
        
        winner = 1
        
    if pink_turtle.xcor() >= 418:
        for i in range(36):
            pink_turtle.right(10)
            pink_turtle.shapesize(3)
            
        winner = 2
        
    if yellow_turtle.xcor() >= 418:
        for i in range(36):
            yellow_turtle.right(10)
            yellow_turtle.shapesize(3)
            
        winner = 3
        
    if red_turtle.xcor() >= 418:
        for i in range(36):
            red_turtle.right(10)
            red_turtle.shapesize(3)
            
        winner = 4

    ############ FINAL SCREEN ############ 
    goto(-550, 300)
    color("darkgreen")
    begin_fill()
    for i in range(2):
        forward(1100)
        right(90)
        forward(600)
        right(90)
    end_fill()

    goto(-270, 0)
    color("white")
    if winner == bet_option:
        write("Congrats! You Win!", font=("Arial", 50, "bold"))
        score = score + bet_amount
    else:
        write("Opps! You Loss!", font=("Arial", 50, "bold"))
        score = score - bet_amount


    # CURRENT PLAYER SCORE
    goto(-170, -100)
    write(f"Your new points is {score}", font=("Arial", 25, "italic"))

    with open("scores.txt", "w") as f:
        f.write(str(score))
    
    time.sleep(4)
    
    again = textinput("Play Again ?", "To play again enter : Y \n Otherwise enter : N").lower()
    if again == "y":
        pass
    elif again == "n":
        break 
    
############### STAGE 3 ########################
bgcolor("black")
goto(-650, 350)
color("black")
begin_fill()
for i in range(2):
    forward(1300)
    right(90)
    forward(700)
    right(90)
end_fill()

speed(0) 
goto(-250, 0)
color("yellow")
write(f"Thank You, {name}.", font=("Arial", 35))

done()