# Task-1
# import random
# n=5
# while(n):
#     coin=random.randint(0,1)
#     if(coin):
#         print("Naukri Milegi next 1 months me!")
#     else:
#         print("Naukri nahi milegi next 1 months me!")
#     n-=1

# Task-2
# You are working in a team of developers.
# Another developer has written the code to import the names in the inputs
# You can run the code to see what this names list looks like.
# Then change the names in the input to see how it imports the names.
# 🚨 Remember to remove the print statement above when you submit.
# input_string = input("Enter a list of name separated by comma :")
# names = input_string.split(",")
# import random
# n=10
# while(n):
#     print(f"{names[random.randint(0,len(names)-1)]} is going to buy the meal today!")
#     n-=1

# Task-3
# line1 = ["⬜️", "️⬜️", "️⬜️"]
# line2 = ["⬜️", "⬜️", "️⬜️"]
# line3 = ["⬜️️", "⬜️️", "⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input()  # Where do you want to put the treasure?
# # 🚨 Don't change the code above 👆
# # Write your code below this row 👇
# row = position[1]
# col = position[0].lower()
# listOfCol = ["a", "b", "c"]
# col = listOfCol.index(col)
# # if(col=="A"):
# #   col=0
# # elif(col=="B"):
# #   col=1
# # else:
# #   col=2

# map[int(row) - 1][col] = "X"
# # print(f"{row} and {col} ")


# # Write your code above this row 👆
# # 🚨 Don't change the code below 👇
# print(f"{line1}\n{line2}\n{line3}")
