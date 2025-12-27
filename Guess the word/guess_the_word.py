import random
from random import sample

countries = ["United States", "Canada", "United Kingdom", "Germany", "Bangladesh", "Japan", "Australia"]
placeholder = ""
chosen_word = random.choice(countries).lower()
print(chosen_word)
for i in range(len(chosen_word)):
    placeholder += '_'

print(placeholder)
display = ""
guess = input("Take a guess. Give me a letter from the Alphabet\n").lower()
for letter in chosen_word:
    if letter == guess:
        display += guess
    else:
        display += "_"

print(display)