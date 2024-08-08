#!usr/bin/python3
import random

rps_array =["rock","paper", "scissors"]

while True:
    try:
        player_choice = input("rock, paper, or scissors? \t")
        computer_choice = random.choice(rps_array)

        if player_choice in rps_array:
            if player_choice == computer_choice:
                print(f"you both chose [{player_choice}], try again")
            elif player_choice == "rock" and computer_choice == "scissors":
                print(f"you win! you chose [{player_choice}] and computer chose [{computer_choice}]")
                break
            elif player_choice == "scissors" and computer_choice == "paper":
                print(f"you win! you chose [{player_choice}] and computer chose [{computer_choice}]")
                break 
            elif player_choice == "paper" and computer_choice == "rock":
                print(f"you win! you chose [{player_choice}] and computer chose [{computer_choice}]")
                break
            else:
                print(f"Sorry you lost! you chose [{player_choice}] and computer chose [{computer_choice}]")
                break
    except Exception:
        print("choose rock, paper, or scissors")

