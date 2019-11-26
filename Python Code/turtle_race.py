# The turtle racing game!
# open the link below!
# github.com/coderdojodit
import turtle
import random

# myTurtle is a variable
myTurtle = turtle.Turtle()
myTurtle.speed(10)
myTurtle.penup()
myTurtle.goto(-140 , 140)

# for loop means repeat 16 times
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


bob = turtle.Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160,50)
bob.pendown()


joseph = turtle.Turtle()
joseph.color('green')
joseph.shape('turtle')

joseph.penup()
joseph.goto(-160,20)
joseph.pendown()


for turn in range(100):
  valentin.forward(random.randint(1,5))
  bob.forward(random.randint(1,5))
  joseph.forward(random.randint(1,5))
  
  
  
  
  
  
  
  
  
  
  
