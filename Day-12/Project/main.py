import random
def chooseMode():
    mode=int(input("\nWhich mode you want to play ? \n1.For Easy \n2.For Hard\n->"))
    if(mode==1):
        chance=10
    elif(mode==2):
        chance=5
    else:
        print("Wrong Choice Choose Again")
        return chooseMode()

    return chance
randomNumber=random.randint(1,100)
chance=chooseMode()
while(chance):
    num=int(input("Guess a Number between 1 to 100: "))
    if(num==randomNumber):
        print(f"You Won your Guess is Correct {num}")
        flag=True
        break
    elif(num>randomNumber):
        print("Too High")
    else:
        print("Too Low")
    chance-=1
    
if(not flag):
    print("You Lost the Game")


