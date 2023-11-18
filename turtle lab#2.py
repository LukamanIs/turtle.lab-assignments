# importing all the libary into python
import turtle
import random

# The variables for the turtle
screen = turtle.Screen()
turtle.speed(2)
bgcolor = str()
color = str()
shape = str()
xpos = int()
ypos = int()
color = color.upper()
shape = shape.upper()

# asking the user for the color of background
bgcolor = screen.textinput("background color","Enter the color of the background screen: ")
#asking for the color of the shape
color = screen.textinput("Turtle color","Enter the color of turtle: ")
# to pick the shape of your choce
shape = screen.textinput("Turtle shape","Enter the shape of the turtle: (classic, arrow, turtle, circle, square and triangle): ")

# putting the bg color in the screen
turtle.bgcolor(bgcolor)
#Putting the shape in the screen
turtle.shape(shape)
#putting the color for the turtle
turtle.color(color)
turtle.penup()


# making the turtle make a circle and making the color black
turtle.goto(100,-200)
turtle.pendown()
turtle.speed(8)
turtle.color("black")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.color(color)

# make the xpos and ypos a variable for turtle
xpos = turtle.xcor()
ypos = turtle.ycor()


# This is the random libary making the code go around the screen so it will start at a random spot in the screen
turtle.penup()
xpos = random.randint(-300,300)
ypos = random.randint(-300,300)
turtle.goto(xpos,ypos)
xpos = random.randint(-300,300)
ypos = random.randint(-300,300)
turtle.goto(xpos,ypos)
xpos = random.randint(-300,300)
ypos = random.randint(-300,300)
turtle.goto(xpos,ypos)
turtle.penup()


# This is the code that will allow the user to go any where in the screen
for steps in range(0,10):
    direction = screen.textinput("direction","Enter F for forward, B for backward,R to move right, L to move left")
    direction = direction.upper()
    if direction == "F":
        turtle.forward(100)
    elif direction == "B":
        turtle.backward(100)
    elif direction == "R":
        turtle.right(90)
        turtle.forward(100)
    elif direction == "L":
        turtle.left(90)
        turtle.forward(100)

    
# this is the code that will tell if you win or lose
x = turtle.xcor()
y = turtle.ycor()
if (x >= 0 and x <= 250) and (y >= -250 and y <= 0):
    turtle.write("You Win!", align="center", font=('Arial', '16', 'bold'))
else:
    turtle.write("Sorry You Lost", align="center", font=('Arial', '16', 'bold'))





