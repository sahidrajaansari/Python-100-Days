# Task:1
# print("Welcome to Rollercoaster!")
# height = int(input("What is your height in cm? "))
# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# Task:2
# Which number do you want to check?
# number = int(input())
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
# if (number & 1) == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# Task:3
# Enter your height in meters e.g., 1.55
# height = 1.55
# # Enter your weight in kilograms e.g., 72
# weight =  72
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bmi = weight / height ** 2
# if bmi < 18.5:
#     print(f"Your BMI is {"{:.1f}".format(bmi)}, you are underweight.")
# elif bmi < 25:
#     print(f"Your BMI is {"{:.1f}".format(bmi)}, you have a normal weight.")
# elif bmi < 30:
#     print(f"Your BMI is {"{:.1f}".format(bmi)}, you are slightly overweight.")
# elif bmi < 35:
#     print(f"Your BMI is {"{:.1f}".format(bmi)}, you are obese.")
# else:
#     print(f"Your BMI is {"{:.1f}".format(bmi)}, you are clinically obese.")

# Task:4
# Which year do you want to check?
# year = int(input())
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
# if( (year%4==0) and (year%100!=0) or (year%400==0)):
#     print("Leap year.")
# else:
#     print("Not Leap year.")

# Task:5
# print("Thank you for choosing Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L\n->") #
# add_pepperoni = input(" Do you want pepperoni? Y or N\n->") #
# extra_cheese = input("Do you want extra cheese? Y or N\n->") #
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# bill=0
# if size == "S":
#     bill = 15
# elif size == "M":
#     bill = 20
# else:
#     bill = 25

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is: ${bill}.")


# Task:6
# print("The Love Calculator is calculating your score...")
# name1 = "Angela Yu"  # What is your name?
# name2 = "Jack Bauer"  # What is their name?
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# countOfTrue = 0
# i = 0
# while i < 4:
#     countOfTrue += name1.count("true"[i])
#     countOfTrue += name2.count("true"[i])
#     countOfTrue += name1.count("TRUE"[i])
#     countOfTrue += name2.count("TRUE"[i])
#     i += 1

# countOfLove = 0
# i = 0
# while i < 4:
#     countOfLove += name1.count("love"[i])
#     countOfLove += name2.count("love"[i])
#     countOfLove += name1.count("LOVE"[i])
#     countOfLove += name2.count("LOVE"[i])
#     i += 1

# score = int(f"{countOfTrue}{countOfLove}")

# if score < 10 or score > 90:
#     print(f"Your score is {score}, you go together like coke and mentos.")
# elif score >= 40 and score <= 50:
#     print(f"Your score is {score}, you are alright together.")
# else:
#     print(f"Your score is {score}.")
