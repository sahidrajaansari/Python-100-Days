from turtle import Screen, Turtle
import random

Screen = Screen()
Screen.setup(width=600, height=600)
# Screen.bgcolor("black")
Screen.title("Etch-a-Sketch")
Screen.bgcolor("black")
choice=Screen.textinput("Bet", "Which turtle will win")


def createTimmy(color="white", y=0):
    timmy = Turtle()
    timmy.color(color)
    timmy.speed(10)
    timmy.shape("turtle")
    timmy.penup()
    timmy.goto(-290, y)
    timmy.pendown()
    return timmy


colors = ["red", "blue", "green", "yellow", "orange", "purple"]
posns = [0, 30, -30, 60, -60]
turtle_list = []

for i in range(5):
    timmy = createTimmy(colors[i], posns[i])
    turtle_list.append(timmy)

flag=True
winner=""   
while flag:
    for timmy in turtle_list:
        timmy.forward(random.randint(1, 10))
        if timmy.xcor() > 290:
            winner=timmy.color()[0]
            flag=False
            break

if choice==winner:
    print(f"You win. The {winner} turtle has won")
else:
    print(f"You lose. The {winner} turtle has won")
            
        
Screen.exitonclick()
