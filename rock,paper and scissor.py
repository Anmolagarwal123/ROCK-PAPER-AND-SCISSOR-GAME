#ROCK PAPER AND SCISSOR GAME

#WE HAVE TO IMPORT THE RANDOM FUNCTION BECAUSE COMPUTER IS CHOOSING A RANDOM NUMBER
print("Let's play a rock,paper and scissor game with the computer!")
import random

player_action = input("Enter a choice (rock,paper,scissor):")
possible_outcomes = ["Rock","Paper","Scissor"]
computer_action = random.choice(possible_outcomes)
print(f"\n User choose {player_action}, Computer choose {computer_action}.\n")

if player_action == computer_action:
    print(f"Both are selected {player_action}. It's a tie!")
elif player_action == "Rock":
    if computer_action == "Scissor":
        print("Rock smashes Scissor!...... You Win!")
    else:
        print("Paper covers rock....... You lose!")
elif player_action == "Paper":
    if computer_action == "Rock":
        print("Paper covers Rock.......You Win!")
    else:
        print("Scissor cuts Paper.......You Lose!")
elif player_action == "Scissor":
    if computer_action == "Paper":
        print("Scissor cuts Paper........You Win!")
    else:
        print("Rock smashes Scissor......You Lose!")
