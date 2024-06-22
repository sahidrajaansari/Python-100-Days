# HangMans Game
import random
import hangman_words
import hangman_art


def hangman():
    wordList = ["aardvark", "baboon", "camel"]
    chosenWord = random.choice(hangman_words.word_list)
    wordLength = len(chosenWord)
    print(f"Chosen word is {chosenWord} abd the length of the word is {wordLength}")
    return chosenWord, wordLength


def checkChar(chosenWord, char):
    if chosenWord.count(char) > 0:
        return True
    else:
        return False


def createDashList(word):
    dashList = []
    for char in word:
        dashList.append("_")
    return dashList


def checkAndAddChar(word, char, currentWordList):
    for i in range(len(word)):
        if word[i] == char:
            currentWordList[i] = char

print(hangman_art.logo)
chosenWord, wordLength = hangman()
alphabet = "abcdefghijklmnopqrstuvwxyz"
currentWordList = createDashList(chosenWord)
currentWordListStr = ""
count = 0


stages = hangman_art.stages

print(f"Guess this Word {currentWordList}")

while (str(currentWordListStr) != chosenWord) and (count < 7):
    # char = random.choice(alphabet)
    char= input("Enter a character: ")
    checkAndAddChar(chosenWord, char, currentWordList)
    currentWordListStr = "".join(currentWordList)

    if not checkChar(chosenWord, char):
        print(f"Wrong guess {char}")
        print(stages[len(stages)-count-1])
        count += 1
    else:
        print(f"Correct guess {char}")
    
    print(f"Current Status of word is {currentWordList}\n")
    


if count == 7:
    print(f"You Lost the game. The word was {chosenWord}")
else:
    print("You Won the game. Congratulations!!!")


