import random

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

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_output = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_output])

if user_choice >=3 or user_choice < 0: 
  print("You chose an invalid number, YOU LOSE!")
else:
  print(game_images[user_choice])        

  if user_choice == 0 and computer_output == 2:
    print("You win!")
  elif computer_output == 0 and user_choice == 2:
    print("You Lose!")
  elif computer_output > user_choice:
    print("You lose!")
  elif user_choice >computer_output:
    print("You Win!")
  elif computer_output == user_choice:
    print("It's a draw... CATS GAME!")
  



