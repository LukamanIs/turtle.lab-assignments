import turtle
import time

# retracting steps function
def retracing_steps():
    # I am making the code move right,left, and forward
    turtle.forward (100)
    turtle.right (90)
    turtle.forward (100)
    turtle.left (90)
    turtle.forward (100)
    turtle.right (90)
    turtle.forward (100)
    turtle.right(90)
    turtle.forward(100)
    turtle.left (180)
    turtle.forward (100)
    turtle.left (90)
    turtle.forward (100)
    turtle.left (90)
    turtle.forward (100)
    turtle.right (90)
    turtle.forward (100)
    turtle.left(90)
    turtle.forward(100)

    
    
#This is the code to draw three shapes which are square,triange, and a circle
def drawing_shapes():
    #This is drawing the circle
    turtle.speed(7)
    turtle.penup()
    turtle.goto(0,120)
    turtle.pendown()
    turtle.color("blue")
    turtle.begin_fill()
    turtle.circle(90)
    turtle.end_fill()
    turtle.color("green")

    turtle.penup()
    turtle.goto(-100,-80)
    turtle.pendown()
    turtle.penup()
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    
    #This is drawing the triangle
    turtle.forward(200)
    turtle.left(120)
    turtle.forward(200)
    turtle.left(120)
    turtle.forward(200)
    turtle.left(120)
    turtle.end_fill()
    turtle.color("green")
    turtle.penup()
    turtle.goto(-100,-100)

    #This is for the square
    turtle.pendown()
    turtle.color("purple")
    turtle.begin_fill()
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.end_fill()
    turtle.color("green")

#This code is to make mult circle one after the other with 4 different colors
def mult_circle():
    horizontal =(-200)
    radius = (25)
    colors = ("yellow", "pink", "orange", "brown")
    pen_size = (4)
    turtle.penup()
    turtle.goto(horizontal,(0))
    #loop to draw the circles
    for count in range (0, 4):
     #set the fill color, pen size and fill color
     turtle.fillcolor(colors[count])
     turtle.pensize(pen_size)
     turtle.begin_fill()
     #draw circles
     turtle.circle(radius)
     #reset locatio, radius and pen size
     horizontal = horizontal + 75
     radius = radius + 20
     pen_size = pen_size + 2
     #moving the turtle
     turtle.penup()
     turtle.goto(horizontal,(0))
     turtle.pendown()
     turtle.end_fill()

#I made this code to write two things in the screen to show that I am done with the code
def end_screen():
    turtle.hideturtle()
    turtle.write("Thank You For Watching", align="center", font=('Arial', '30', 'bold'))
    time.sleep(3)
    turtle.clearscreen()
    turtle.bgcolor("grey")
    turtle.write("The End!", align="center", font=('Arial', '30', 'bold'))
    
    
#Now I put it all together in the main funtion
def main():
    turtle.bgcolor("grey")
    retracing_steps()
    time.sleep(3)
    turtle.reset()
    drawing_shapes()
    time.sleep(3)
    turtle.reset()
    mult_circle()
    time.sleep(3)
    turtle.reset()
    end_screen()

main()


