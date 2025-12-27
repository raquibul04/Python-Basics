import random
from random import sample

countries = ["United States", "Canada", "United Kingdom", "Germany", "Bangladesh", "Japan", "Australia"]

chosen_word = random.choice(countries).lower()
print(chosen_word)
guess = input("Take a guess. Give me a letter from the Alphabet\n").lower()
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

placeholder = ' _ ' * len(chosen_word)
print(placeholder)