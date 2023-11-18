import turtle

# turtle outline
turtle.shape("turtle")
turtle.color("green")
turtle.bgcolor("black")
turtle.speed(4)
turtle.pencolor("green")

# outline square
turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()
turtle.begin_fill()
turtle.pensize(5)
turtle.color("magenta")

turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.end_fill()

# outline circle
turtle.penup()
turtle.color("green")
turtle.goto(200, 100)
turtle.pendown()
turtle.pensize(10)
turtle.color("blue")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

# outline for triangle
turtle.penup()
turtle.color("green")
turtle.goto(-300, 100)
turtle.pendown()
turtle.pensize(7)
turtle.color("red")
turtle.begin_fill()

turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.left(120)
turtle.end_fill()

#change location
turtle.penup()
turtle.color("green")
turtle.goto(0, 0)
turtle.pendown()

turtle.hideturtle()
turtle.exitonclick()
