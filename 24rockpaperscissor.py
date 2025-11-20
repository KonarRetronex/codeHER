import random

option = ["rock", "paper", "scissors"]
running = True

while running == True:
    player = None
    computer = random.choice(option)

    while player not in option:
        player = input("Enter a choice(rock/paper/scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Draw")
    elif player == "rock" and computer == "scissors":
        print("You win")
    elif player == "paper" and computer == "rock":
        print("You win")
    elif player == "scissors" and computer == "paper":
        print("You win")
    else:
        print("You lose")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == "y":
        running = True
    else:
        running = False

print("Thank you for playing!")
