# Tip Calculator

## Overview
The Tip Calculator is a simple Python program that helps split a restaurant bill among multiple people, including a selected tip percentage.

## Features
- Takes total bill amount as input
- Allows tip percentage selection (10, 12, or 15)
- Splits the bill evenly among people
- Rounds the final amount per person

## How It Works
1. Enter the total bill amount
2. Choose a tip percentage
3. Enter the number of people
4. The program calculates and displays how much each person should pay

## Code
```python
print("Welcome to the Tip Calculator!")
bill = int(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

bill_with_tip = round((bill + bill * (tip / 100)) / people)

print(f"Each person should pay: {bill_with_tip}")
