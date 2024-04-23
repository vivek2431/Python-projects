# Rock Paper Scossors game

import random

user_choice=int(input("Enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissors"))
if user_choice >= 3 or user_choice <0:
    print("You entered invalid number, You Lose.")
else:
    computer_choice=random.randint(0,2)
    print("Computer Chose:")
    print(computer_choice)
    if computer_choice == user_choice:
     print("It's draw.")
    elif computer_choice == 0 and user_choice == 2:
     print("You Lose.")
    elif user_choice == 0 and computer_choice ==2:
     print("You Win.")
    elif computer_choice > user_choice:
     print("You Lose.")
    elif user_choice > computer_choice:
     print("You Win.")

# Output : Enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissors2
Computer Chose:
2
It's draw.
Enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissors1
Computer Chose:
0
You Win.
Enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissors5
You entered invalid number, You Lose.
Computer Chose:
2
