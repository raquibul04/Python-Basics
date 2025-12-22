# PyPassword Generator 🔐

## Overview
PyPassword Generator is a simple Python program that creates a **random password**
based on user-defined criteria. The user chooses how many **letters**, **numbers**,
and **symbols** the password should contain, and the program generates a shuffled,
randomized password accordingly.

---

## Features
- User-defined password length
- Includes:
  - Lowercase letters (a–z)
  - Numbers (0–9)
  - Common symbols (! @ # $ % ^ & * ( ))
- Randomized order for better security
- Easy to understand and beginner-friendly

---

## How It Works

1. Predefined lists are created for:
   - Letters
   - Numbers
   - Symbols
2. The user is prompted to enter how many of each character type they want.
3. The program:
   - Randomly selects characters using `random.sample()`
   - Combines all selected characters into one list
   - Shuffles the list using `random.shuffle()`
   - Converts the shuffled list into a string
4. The final password is displayed.

---
5. Run the program:
   ```bash
   python rock_paper_scissors.py




