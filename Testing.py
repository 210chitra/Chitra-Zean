# name:_chitra zean
# profession: corin
# date:04/18/2025


import random
options = ("rock", "paper", "scissors")



running = True
winner_score = 5
player_score = 0
computer_score = 0


while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice(rock,paper,scissors):")

    print(f"Play: {
        computer_score = computer_score + 1

    # TODO: check the scores. If they are 5 that player/computer wins

    # TODO then ask if they want to play again

    print(f"player score:{player_score}")
    print(f"computer score:{computer_score}")


    # play_again = input("play again? (y/n):")
    # if not play_again.lower() == "y":
    #     running = False


print("Thanks for playing!")player}")
    print(f"computer: {computer}")

    if player == computer:
        print("it's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
        player_score = player_score + 1
    elif player == "paper" and computer == "rock":
        print("You win!")
        player_score = player_score + 1
    elif player == "scissors" and computer == "paper":
        print("You win!")
        player_score = player_score + 1
    else:
        print("You lose!")