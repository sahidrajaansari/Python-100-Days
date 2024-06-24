# Black-Jack Game
import random
deckOfCards = [
    {
        "CardName": "Ace",
        "CardValue":  11,
    },
    {
        "CardName": "Two",
        "CardValue": 2,
    },
    {
        "CardName": "Three",
        "CardValue": 3,
    },
    {
        "CardName": "Four",
        "CardValue": 4,
    },
    {
        "CardName": "Five",
        "CardValue": 5,
    },
    {
        "CardName": "Six",
        "CardValue": 6,
    },
    {
        "CardName": "Seven",
        "CardValue": 7,
    },
    {
        "CardName": "Eight",
        "CardValue": 8,
    },
    {
        "CardName": "Nine",
        "CardValue": 9,
    },
    {
        "CardName": "Ten",
        "CardValue": 10,
    },
    {
        "CardName": "Jack",
        "CardValue": 10,
    },
    {
        "CardName": "Queen",
        "CardValue": 10,
    },
    {
        "CardName": "King",
        "CardValue": 10,
    },
]

def dealCard():
    return random.choice(deckOfCards)

def calculateScore(cards):
    score = 0
    for card in cards:
        score += card["CardValue"]
    return score

def returnCards(cardList):
    cardNames=[]
    for card in cardList:
        cardNames.append(card["CardName"])
    return cardNames

def scoreOfCards(cardList):
    score=0
    flag=False
    for card in cardList:
        if(card["CardName"]=="Ace"):
            flag=True
        score+=card["CardValue"]

    if(flag and score>21):
        score-=10
    
    return score

computerCards = []
playerCards = []
computerCards.append(dealCard())
playerCards.append(dealCard())
print(f"Computer Cards are \n{returnCards(computerCards)} and currentScore is {scoreOfCards(computerCards)}")
computerCards.append(dealCard())
playerCards.append(dealCard())
print(f"Your cards are \n{returnCards(playerCards)} and currentScore is {scoreOfCards(playerCards)}")
drawMore=True
currentPlayerScore=scoreOfCards(playerCards)
while(drawMore and currentPlayerScore<21):
    k=str(input("\nDo you Want to draw more cards ? 1.Yes 2.No\n"))
    if(k.lower()=="yes" and currentPlayerScore<21):
        playerCards.append(dealCard())
        currentPlayerScore=scoreOfCards(playerCards)
        print(f"Your cards are \n{returnCards(playerCards)}  and currentScore is {scoreOfCards(playerCards)}")
    else:
        drawMore=False
currentPlayerScore=scoreOfCards(playerCards)
if(currentPlayerScore>21):
    print("You Lost the Game")
    print(f"Computers Cards Were {returnCards(computerCards)}")
    exit()

currentComputerScore=scoreOfCards(computerCards)
while(currentComputerScore<=21):
    k=random.randint(0,1)
    if(k==1):
        computerCards.append(dealCard())
        currentComputerScore=scoreOfCards(computerCards)
    else:
        break
currentComputerScore=scoreOfCards(computerCards)

if((21-currentComputerScore)==(21-currentPlayerScore)):
    print("Game is Draw")
    print(f"Computers Cards Were {returnCards(computerCards)}")
    print(f"and your Cards were {returnCards(playerCards)}")
elif( currentComputerScore<=21 and (21-currentComputerScore)<(21-currentPlayerScore)):
    print("You Lost the Game")
    print(f"Computers Cards Were {returnCards(computerCards)}")
    print(f"and your Cards were {returnCards(playerCards)}")
else:
    print("You Won the Game")
    print(f"Computers Cards Were {returnCards(computerCards)}")
    print(f"and your Cards were {returnCards(playerCards)}")
