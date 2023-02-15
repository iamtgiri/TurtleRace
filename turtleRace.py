from turtle import *
from random import *
import turtle
import time  

# SCREEN SETUP 
setup(1200, 700)
title("The Turtle Race")
bgcolor("forestgreen")
speed(0) 

# HEADINGS 
penup()
goto(-150,310)
color("white")
write("THE TURTLE RACE", font=("Arial", 20, "bold"))

# DIRT 
goto(-550, 300)
pendown()
color("green")
begin_fill()
for i in range(2):
    forward(1100)
    right(90)
    forward(600)
    right(90)
end_fill()
penup()

# BOUNDARY 
goto(-550, 300)
pendown()
width(4)
color("white")
for i in range(2):
    forward(1100)
    right(90)
    forward(600)
    right(90)

# FINISH LINE 
gap_size = 10
shape("square")
penup()

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

# PROMPT SETUP
bet_option = textinput(title = "Make Your Bet", prompt="Which turtle will win the game? choose a number from the color list : 1.purple, 2.blue, 3.yellow, 4.red.")

with open("D:\\Visual code\\python programming\\TurtleRace\\scores.txt") as f:
    score = int(f.read())

bet_amount = int(textinput(title="Enter Amount", prompt=f"you have {score} points. how much you want to invest?"))

# PAUSE 
time.sleep(0.5)

# MOVEMENT
while blue_turtle.xcor() <= 418 and pink_turtle.xcor() <= 418 and yellow_turtle.xcor() <= 418 and red_turtle.xcor() <= 418:
    
    if blue_turtle.ycor() >= 275:
        blue_turtle.right(45)
        blue_turtle.forward(5)
    if blue_turtle.ycor() <= -275:
        blue_turtle.right(-45)
        blue_turtle.forward(5)
    if  blue_turtle.xcor() <= -505:
        blue_turtle.right(-135)
    blue_turtle.forward(randint(1,10))
    blue_turtle.right(randint(-10,10))
    
    if pink_turtle.ycor() >= 275:
        pink_turtle.right(90)
        pink_turtle.forward(5)
    if pink_turtle.ycor() <= -275:
        pink_turtle.right(-90)
        pink_turtle.forward(5)
    if  pink_turtle.xcor() <= -505:
        pink_turtle.right(-135)
    pink_turtle.forward(randint(1,10))
    pink_turtle.right(randint(-10,10))
    
    if yellow_turtle.ycor() >= 275:
        yellow_turtle.right(90)
        yellow_turtle.forward(5)
    if yellow_turtle.ycor() <= -275:
        yellow_turtle.right(-90)
        yellow_turtle.forward(5)
    if  yellow_turtle.xcor() <= -505:
        yellow_turtle.right(-135)
    yellow_turtle.forward(randint(1,10))
    yellow_turtle.right(randint(-10,10))
    
    if red_turtle.ycor() >= 275:
        red_turtle.right(90)
        red_turtle.forward(5)
    if red_turtle.ycor() <= -275:
        red_turtle.right(-90)
        red_turtle.forward(5)
    if  red_turtle.xcor() <= -505:
        red_turtle.right(-135)
    red_turtle.forward(randint(1,10))
    red_turtle.right(randint(-10,10))

# RESULT 
if blue_turtle.xcor() >= 418:
    for i in range(72):
        blue_turtle.right(5)
        blue_turtle.shapesize(3)
        
    goto(-550, 300)
    pendown()
    color("darkgreen")
    begin_fill()
    for i in range(2):
        forward(1100)
        right(90)
        forward(600)
        right(90)
    end_fill()
    # penup()
    goto(-270, 0)
    color("white")
    write("Purple Turtle Wins!", font=("Arial", 50, "bold"))
    
    
if pink_turtle.xcor() >= 418:
    for i in range(72):
        pink_turtle.right(5)
        pink_turtle.shapesize(3)
        
    goto(-550, 300)
    pendown()
    color("darkgreen")
    begin_fill()
    for i in range(2):
        forward(1100)
        right(90)
        forward(600)
        right(90)
    end_fill()
    # penup()
    goto(-270, 0)
    color("white")
    write("White Turtle Wins!", font=("Arial", 50, "bold"))
    
if yellow_turtle.xcor() >= 418:
    for i in range(72):
        yellow_turtle.right(5)
        yellow_turtle.shapesize(3)
        
    goto(-550, 300)
    pendown()
    color("darkgreen")
    begin_fill()
    for i in range(2):
        forward(1100)
        right(90)
        forward(600)
        right(90)
    end_fill()
    # penup()
    goto(-270, 0)
    color("white")
    write("Yellow Turtle Wins!", font=("Arial", 50, "bold"))
    
if red_turtle.xcor() >= 418:
    for i in range(72):
        red_turtle.right(5)
        red_turtle.shapesize(3)
        
    goto(-550, 300)
    pendown()
    color("darkgreen")
    begin_fill()
    for i in range(2):
        forward(1100)
        right(90)
        forward(600)
        right(90)
    end_fill()
    # penup()
    goto(-270, 0)
    color("white")
    write("Red Turtle Wins!", font=("Arial", 50, "bold"))

penup()
done()