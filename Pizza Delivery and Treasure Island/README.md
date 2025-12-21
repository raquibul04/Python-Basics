# Python Mini Projects (2 Scripts)

This folder contains **two beginner Python scripts**:
1. `pizza_delivery.py` — calculates a pizza order total based on size and add-ons
2. `treasure_island.py` — a text-based adventure game where choices decide the outcome

---

## Files

- **pizza_delivery.py**
  - Purpose: Calculate the final pizza bill based on user selections
  - Concepts: input handling, conditionals (`if/elif/else`), basic arithmetic

- **treasure_island.py**
  - Purpose: Play a simple adventure game where the player makes decisions to find treasure
  - Concepts: nested conditionals, input handling, control flow, branching logic

---

## 1) Pizza Delivery 🍕

### What it does
The script asks the user:
- Pizza size: `S`, `M`, or `L`
- Pepperoni: `Y` or `N`
- Extra cheese: `Y` or `N`

Then it calculates and prints the total bill.

### Pricing Rules
- **Small (S)**: $15  
  - Pepperoni: +$2  
  - Extra cheese: +$1  

- **Medium (M)**: $20  
  - Pepperoni: +$3  
  - Extra cheese: +$1  

- **Large (L)**: $25  
  - Pepperoni: +$3  
  - Extra cheese: +$1  


# Treasure Island 🏝️

## Overview
Treasure Island is a **text-based adventure game written in Python**.  
The player must make the correct sequence of choices to survive and find the hidden treasure.

Each decision affects the outcome — one wrong move results in **Game Over**.

---

## Objective
Navigate through a series of choices and reach the treasure by making the correct decisions.

---

## How the Game Works
1. The game starts at a crossroads.
2. The player chooses to go **left** or **right**.
3. If the player goes left, they must choose to **swim** or **wait**.
4. If the player waits, they must choose a door:
   - **Red** → Burned by fire (Game Over)
   - **Blue** → Eaten by beasts (Game Over)
   - **Yellow** → Treasure found (You Win!)
5. Any wrong choice ends the game.

---

## Concepts Practiced
- User input handling
- Nested `if / elif / else` statements
- String normalization using `.lower()`
- Control flow and decision-based logic

---

## How to Run
1. Make sure Python 3 is installed.
2. Save the script as `treasure_island.py`. or `pizza_delivery.py`
3. Run the program:
   ```bash
   python treasure_island.py 
   or
   python pizza_delivery.py
   



