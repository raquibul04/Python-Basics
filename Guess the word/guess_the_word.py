import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6
countries = ["Canada", "Germany", "Bangladesh", "Japan", "Australia"]
placeholder = ""
chosen_word = random.choice(countries).lower()
print(chosen_word)
for i in range(len(chosen_word)):
    placeholder += '_'
print(placeholder)

game_over = False
correct_letters = []
while not game_over:
    display = ""
    guess = input("Take a guess. Give me a letter from the Alphabet\n").lower()
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You loose")
    if "_" not in display:
        game_over = True
    lives -= 1
    print(stages[lives])
