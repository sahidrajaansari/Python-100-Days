import random

listOfBidders={}
def getBidder():
    name=str(input("Enter Your Name : "))
    amount=float((input("Bid between 0 and 1 : $")))
    listOfBidders[name]=amount


bidderAvilable=True
while(bidderAvilable):
    getBidder()
    check=str(input("Are there more bidders Avilable? 1.Yes 2.No \n->"))
    if(check.lower()=='no'):
        bidderAvilable=False

winningBid = random.uniform(0, 1)
print("The winning bid is:", winningBid)

currentLowestBid=2
currentWinner=""
for user in listOfBidders:
    if(currentLowestBid>abs(listOfBidders[user]-winningBid)):
        currentWinner=user
        currentLowestBid=abs(listOfBidders[user]-winningBid)

print(f"Winner of the bid is {currentWinner} and he bided for {listOfBidders[currentWinner]}")

