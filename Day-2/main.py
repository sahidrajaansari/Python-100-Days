# Strings
# Task: 1
# print("Hello World"[2])
# Python ignores underscores in numbers
# print(123_456_789)
# print(str(type(123.23 + 23.23)) +" " + str(123.23 + 23.23))

# Task: 2
# print(70 + float("100.5"))
# print(str(70) + str(100.5))


# Task: 3
# two_digit_number = input()
# # 🚨 Don't change the code above 👆
# ####################################
# # Write your code below this line 👇
# sum=0
# two_digit_number=int(two_digit_number)
# while(two_digit_number):
#     num=two_digit_number%10
#     print(num)
#     sum+=num
#     two_digit_number/=10
#     two_digit_number=int(two_digit_number)
# print((sum))

# two_digit_number = input()
# # 🚨 Don't change the code above 👆
# ####################################
# # Write your code below this line 👇
# print(int(two_digit_number[0])+int(two_digit_number[1]))


# Task: 4
# PEMDAS
# Parentheses
# Exponents
# Multiplication and Division (left-to-right)
# Addition and Subtraction (left-to-right)
# print(3 * (3 + 3) / 3 - 3 ** 2)

# Task: 5
# 1st input: enter height in meters e.g: 1.65
# height = input()
# height = 1.65
# # 2nd input: enter weight in kilograms e.g: 72
# # weight = input()
# weight = 72
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# BMI=(float(weight))/(float(height)**2)
# print(round(BMI,2))


# Task: 6
# score = 0
# score+=1
# print("Your Score is " + str(score))

# Task: 7
# score = 0
# height = 1.65
# isWinning = True
# print("Your score is " + str(score) + " Your height is " + str(height) + " You are winning is " + str(isWinning))
# print(f"Your score is {score}, Your height is {height}, You are winning is {isWinning}")


# Task: 8
# age = input()
age=15
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
yearsLeft = 90 - int(age)
weeksLeft = yearsLeft * 52
print(f"You have {weeksLeft} weeks left.")