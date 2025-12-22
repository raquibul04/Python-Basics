import random
print("Welcome to the Rock, Paper, Scissors game!")
gamer = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors"))
rock = ''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_image = [rock,paper,scissors]

computer = random.randint(0,2)
if gamer == 0 and computer == 1:
    print(f"Your choice: {game_image[gamer]} and Computer's choice: {game_image[computer]}")
    print("You picked Rock and Computer picked Paper.\nComputer won!")
elif gamer == 0 and computer == 2:
    print(f"Your choice: {game_image[gamer]} and Computer's choice: {game_image[computer]}")
    print("You picked Rock and Computer picked Scissors.\n You won!")
elif gamer == 1 and computer == 0:
    print(f"Your choice: {game_image[gamer]} and Computer's choice: {game_image[computer]}")
    print("You picked Paper and Computer picked Rock.\n You won!")
elif gamer == 1 and computer == 2:
    print(f"Your choice: {game_image[gamer]} and Computer's choice: {game_image[computer]}")
    print("You picked paper and Computer picked Scissors.\n Computer won!")
elif gamer == 2 and computer == 0:
    print(f"Your choice: {game_image[gamer]} and Computer's choice: {game_image[computer]}")
    print("You picked Scissors and the computer picked Rock.\n Computer won!")
elif gamer ==2 and computer == 1:
    print(f"Your choice: {game_image[gamer]} and Computer's choice: {game_image[computer]}")
    print("You picked Scissors and computer picked paper.\n You won!")
else:
    print(f"Your choice: {game_image[gamer]} and Computer's choice: {game_image[computer]}")
    print("The game is draw")