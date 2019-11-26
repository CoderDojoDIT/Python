# The turtle racing game!
import turtle

myTurtle = turtle.Turtle()
myTurtle.penup()
myTurtle.goto(-140 , 140)

for step in range(16):
    myTurtle.write(step)
    myTurtle.right(90)
    myTurtle.forward(10)
    myTurtle.pendown()
    myTurtle.forward(150)
    myTurtle.penup()
    myTurtle.backward(160)
    myTurtle.left(90)
    myTurtle.forward(20)

valentin = turtle.Turtle()
valentin.color('red')
valentin.shape('turtle')

valentin.penup()
valentin.goto(-160,100)
valentin.pendown()
