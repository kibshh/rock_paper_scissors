import pictures
import random

choice = 4

while choice not in [0, 1, 2]:
    try:
        choice = int(input("Choose one:\n0 for ROCK \n1 for PAPER \n2 for SCISSORS\nInput here: "))
    except ValueError:
        print("Invalid input, please enter a valid integer.")
print("You chose:")
print(pictures.array_of_pics[choice])

print("Computer chose:")
computer_choice = random.randint(0,2)

print(pictures.array_of_pics[computer_choice])

if choice == computer_choice:
    print("It's a draw.")
elif choice == 0 and computer_choice == 1:
    print("You lose.")
elif choice == 1 and computer_choice == 2:
    print("You lose.")
elif choice == 2 and computer_choice == 0:
    print("You lose.")
elif choice == 1 and computer_choice == 0:
    print("You win!")
elif choice == 2 and computer_choice == 1:
    print("You win!")
elif choice == 0 and computer_choice == 2:
    print("You win!")