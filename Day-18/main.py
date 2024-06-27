# from turtle import Turtle, Screen
# import turtle as t

# timmy = Turtle()
# # timmy.shape("turtle")
# # timmy.color("pink")

# # Challeng-1
# # timmy.forward(50)

# # timmy.right(90)
# # timmy.forward(100)

# # timmy.right(90)
# # timmy.forward(100)

# # timmy.right(90)
# # timmy.forward(100)

# # timmy.right(90)
# # timmy.forward(50)


# # Challenge-2
# # for _ in range(10):
# #     timmy.forward(10)
# #     timmy.penup()
# #     timmy.forward(10)
# #     timmy.pendown()

# # challenge-3
# # length=50
# # side=3
# # angle=360/side
# # for _ in range(20):
# #     if(side==3):
# #         timmy.color("crimson")
# #     elif(side==4):
# #         timmy.color("light sky blue")
# #     elif(side==5):
# #         timmy.color("medium spring green")
# #     elif(side==6):
# #         timmy.color("pink")
# #     elif(side==7):
# #         timmy.color("purple")
# #     elif(side==8):
# #         timmy.color("orange")
# #     elif(side==9):
# #         timmy.color("black")
# #     elif(side==10):
# #         timmy.color("pale violet red")
# #     elif(side==11):
# #         timmy.color("turquoise")
# #     elif(side==12):
# #         timmy.color("aquamarine")
# #     elif side == 13:
# #         timmy.color("red")
# #     elif side == 14:
# #         timmy.color("blue")
# #     elif side == 15:
# #         timmy.color("green")
# #     elif side == 16:
# #         timmy.color("yellow")
# #     elif side == 17:
# #         timmy.color("brown")
# #     elif side == 18:
# #         timmy.color("gray")
# #     elif side == 19:
# #         timmy.color("magenta")
# #     elif side == 20:
# #         timmy.color("cyan")
# #     elif side == 21:
# #         timmy.color("gold")
# #     print(f"length:{length} side:{side} angle:{angle}")
# #     for i in range(side):
# #         timmy.forward(length)
# #         timmy.right(angle)
# #     side+=1
# #     angle=360/side

# # Challenge-4
# # colors = [
# #     "crimson",
# #     "light sky blue",
# #     "medium spring green",
# #     "pink",
# #     "purple",
# #     "orange",
# #     "black",
# #     "pale violet red",
# #     "turquoise",
# #     "aquamarine",
# #     "red",
# #     "blue",
# #     "green",
# #     "yellow",
# #     "brown",
# #     "gray",
# #     "magenta",
# #     "cyan",
# #     "gold",
# # ]
# import random
# t.colormode(255)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color


# # timmy.speed("fastest")
# # for _ in range(random.randint(100, 200)):
# #     timmy.pencolor(random_color())
# #     timmy.forward(30)
# #     timmy.pensize(random.randint(1, 10))
# #     timmy.setheading(random.choice([0, 90, 180, 270]))


# # Challenge-5
# timmy.speed("fastest")
# timmy.circle(30)
# for i in range(360):
#     timmy.circle(100)
#     timmy.right(1)
#     timmy.pencolor(random_color())


# screen = Screen()
# screen.exitonclick()
