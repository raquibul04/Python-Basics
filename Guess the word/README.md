# Hangman Game (Python)

## 📌 Overview
This is a command-line Hangman game written in Python.  
The program randomly selects a country name and asks the player to guess it one letter at a time. Each incorrect guess reduces the player’s remaining lives and visually updates the Hangman drawing.

---

## 🎮 How the Game Works
- A random country is selected from a predefined list
- The word is hidden using underscores (_)
- The player guesses one letter per turn
- Correct guesses reveal letters in the word
- Incorrect guesses reduce lives and advance the Hangman stage
- The game ends when:
  - The word is fully guessed (Win)
  - OR the player runs out of lives (Lose)

---

## 🧩 Game Components

### Hangman Stages
The game uses ASCII art to visually display the Hangman.  
Each stage corresponds to the number of remaining lives.

### Lives Counter
The player starts with 6 lives. Each incorrect guess reduces the life count.

### Word Selection
A random country is chosen from a predefined list and converted to lowercase for consistency.

### Placeholder Creation
Before the game starts, underscores are generated to match the length of the chosen word.

### Game Loop
The game runs inside a while loop until the game is over.  
Each loop:
- Prompts the user for a letter
- Updates the displayed word
- Tracks correct guesses
- Reduces lives if the guess is wrong
- Prints the current Hangman stage

### Letter Matching Logic
- If the guessed letter matches a letter in the word, it is revealed
- If the letter was guessed correctly earlier, it remains visible
- Otherwise, an underscore is shown

### Win & Lose Conditions
- If there are no underscores left, the player wins
- If lives reach zero, the player loses

---

## ❗ Important Logic Issue (Bug Awareness)
The lives counter is reduced twice during each loop iteration:
- Once when the guess is incorrect
- Once again at the end of the loop

This causes lives to drop faster than intended.

Recommended fix:
Remove the extra life reduction so lives decrease only when a guess is incorrect.

---

## ▶️ How to Run the Game
1. Save the Python file as hangman.py
2. Ensure Python 3 is installed
3. Run the program using:
   python hangman.py

---

## 🧠 What This Project Teaches
- while and for loops
- Conditional logic (if / elif / else)
- String manipulation
- Lists and indexing
- Basic game-state management

---

## 🚀 Possible Improvements
- Prevent duplicate guesses
- Track incorrect guesses separately
- Add difficulty levels
- Use a larger or external word list
- Refactor logic into functions

---

Enjoy playing and improving the Hangman game!
