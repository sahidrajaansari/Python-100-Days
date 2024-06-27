from color_extractor import list_of_colors
import turtle as t
import random

t.colormode(255)
t.hideturtle()
t.speed("fastest")

# Set the starting position of the turtle
t.penup()
t.setpos(-200, -200)

for i in range(10):
    for j in range(10):
        t.dot(20, random.choice(list_of_colors))
        t.forward(50)
    t.setpos(-200, t.ycor() + 50)

screen = t.Screen()
screen.exitonclick()