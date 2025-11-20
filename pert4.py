import random
import time

options = ("rock", "paper", "scissors")
# player = None
computer = random.choice(options)
running = True

while running == True:
    player = input("Masukkan (rock/paper/scissors): ")

    while player not in options:
        player = input("Masukkan (rock/paper/scissors): ")

    print(f"player's choice: {player} ")
    time.sleep(1)
    print(f"computer's choice: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == "y":
        running = True
    else:
        running = False
print("Terimakasih Telah Bermain")