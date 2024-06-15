# Tip-Calculator
print("Welcome to the tip calculator.")
total_bill = float(input("Enter the total bill amount in rupees: ₹"))
tip_percentage = float(input(("Enter the tip percentage you would like to give. 10, 12, or 15? \n->")))
total_bill = total_bill + total_bill * (tip_percentage / 100)
total_people = int(input("Enter the number of people to split the bill ? \n->"))
bill_per_person = total_bill / total_people

print(f"Each person should pay: ₹{"{:.2f}".format(round(bill_per_person, 2))}")