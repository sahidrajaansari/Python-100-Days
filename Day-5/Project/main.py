# Password-Generator
import random

smallCaseAlphabets = "abcdefghijklmnopqrstuvwxyz"
capitalCaseAlphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
specialCharacters = "!@#$%^&*()_+"
password = ""

print("Welcome to the PyPassword Generator!")
numberOfLetters = int(input("How many letters would you like in your password?\n"))
numberOfNumbers = int(input("How many numbers would you like?\n"))
numberOfSpecialCharacters = int(input("How many special characters would you like?\n"))

totalLength = numberOfLetters + numberOfNumbers + numberOfSpecialCharacters

for i in range(0, numberOfLetters):
    password += random.choice(smallCaseAlphabets + capitalCaseAlphabets)

for i in range(0, numberOfNumbers):
    randomIndex = random.randint(0, len(password) - 1)
    password = password[:randomIndex] + random.choice(numbers) + password[randomIndex:]

for i in range(0, numberOfSpecialCharacters):
    randomIndex = random.randint(0, len(password) - 1)
    password = (
        password[:randomIndex]
        + random.choice(specialCharacters)
        + password[randomIndex:]
    )

print(f"Your password is: {password}")
