# from turtle import Turtle, Screen

# timmy = Turtle()
# screen = Screen()
# timmy.shape("turtle")
# timmy.color("red")

# while(True):
#     move=str(input("Press Enter F moving forward , b for Backwared, l for left and 'q' for quit: "))
#     if move.lower()=='f':
#         timmy.forward(10)
#     elif move.lower()=='b':
#         timmy.backward(10)
#     elif move.lower()=='l':
#         timmy.left(90)
#         timmy.forward(10)
#     elif move.lower()=='q':
#         break

# print(screen.canvheight)

# screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Pokemon", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])
print(table)
table.align = "l"
print(table)