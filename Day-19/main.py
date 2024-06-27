import turtle as t
import random

timmy=t.Turtle()
def forward():
    timmy.forward(10)
def backward():
    timmy.backward(10)
def left():
    current_heading = timmy.heading()+10
    timmy.setheading(current_heading)
def right():
    current_heading = timmy.heading()-10
    timmy.setheading(current_heading)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

t.listen()
t.onkey(forward,"w")
t.onkey(backward,"s")
t.onkey(left,"a")
t.onkey(right,"d")
t.onkey(clear,"c")

screen = t.Screen()
screen.exitonclick()
