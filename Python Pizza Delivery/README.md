# Python Pizza Deliveries 🍕

## Overview
Python Pizza Deliveries is a simple Python program that calculates the total cost of a pizza order based on size and selected toppings.

The user chooses:
- Pizza size (Small, Medium, or Large)
- Whether to add pepperoni
- Whether to add extra cheese

The program then calculates and displays the final bill.

---

## Features
- Supports three pizza sizes: S, M, L
- Optional pepperoni topping
- Optional extra cheese
- Automatic price calculation
- Case-insensitive input handling

---

## Pricing Rules
- Small (S): $15
  - Pepperoni: +$2
  - Extra cheese: +$1

- Medium (M): $20
  - Pepperoni: +$3
  - Extra cheese: +$1

- Large (L): $25
  - Pepperoni: +$3
  - Extra cheese: +$1

---

## Code
```python
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

bill = 0
if size == "S":
    bill += 15
    if pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
elif size == "M":
    bill += 20
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
elif size == "L":
    bill += 25
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1

print(f"Your total bill is {bill}")
