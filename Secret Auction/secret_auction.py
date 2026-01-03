
new_bid = True
auction = {}
highest_bid =0
while new_bid:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bid = input("Do want to bid again? Type 'Yes' or 'No'").lower()
    auction[name]=price
    if bid == 'no':
        new_bid = False
    if price > highest_bid:
        highest_bid = price
        print(f"{name} is the highest bidder with ${highest_bid}")
