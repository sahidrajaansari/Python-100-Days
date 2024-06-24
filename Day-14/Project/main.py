import random
import art
import game_data
import os

def getUser():
    user=random.choice(game_data.data)
    return user

def printUser(user):
    print(f"Name: {user['name']}")
    print(f"Description: {user['description']}")
    print(f"Country: {user['country']}")

def compareUser(user1,user2,choice):
    if choice == 1:
        if user1["follower_count"] < user2["follower_count"]:
            return False
        elif user1["follower_count"] > user2["follower_count"]:
            return True
        else:
            print("Both users have the same number of followers.")
            return False
    elif choice == 2:
        if user1["follower_count"] > user2["follower_count"]:
            return False
        elif user1["follower_count"] < user2["follower_count"]:
            return True
        else:
            print("Both users have the same number of followers.")
            return False
    else:
        print("Invalid choice. Please enter 1 or 2.")
        return False
    return False

user1=getUser()
user2=getUser()
print(art.logo)
count=0
while(True):
    print("contestant-1")
    printUser(user1)
    print(art.vs)
    print("contestant-2")
    printUser(user2)
    choice=int(input("\nSelect 1 for the first contestant or 2 for the second contestant: "))
    if(compareUser(user1,user2,choice)):
        count+=1
        if(choice==2):
            user1=user2
        user2=getUser()
    else:
        print(f"Game Over your score is {count} and {user1['name']} has {user1["follower_count"]} and {user2['name']} has {user2["follower_count"]}")
        break
    os.system("cls")
