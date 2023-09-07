import random

user_action = input("Enter your coice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_act}, computer chose {computer_act}.\n")

if user_act == computer_act:
    print(f"Both players selected {user_act}. It's a tie!")
elif user_action == "rock":
    if computer_act == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_acti == "paper":
    if computer_act "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_act == "scissors":
    if computer_act == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
