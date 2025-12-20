print("Welcome to the Tip Calculator!")
bill = int(input("What was the total bill?"))
tip = int (input ("How much tip would you like to give? 10,12, or 15?"))
people = int (input("How many people to split the bill?"))

bill_with_tip = round((bill + bill*(tip/100))/people)

print(f"Each person should pay: {bill_with_tip}")