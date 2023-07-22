import turtle
import random

SIZE = 80
DISTANCE = 100

colors = ["red","blue","green"]

turtle.penup()
turtle.backward(140)
turtle.pendown()

for x in range(1,4):
    turtle.pendown()
    turtle.fillcolor(colors[x-1])
    turtle.begin_fill()
    for _ in range(0,4):   
        turtle.forward(SIZE)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(DISTANCE)

turtle.exitonclick()