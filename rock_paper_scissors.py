import random
import time

throws = ["rock", "paper", "scissors"]


def throw_outcomes():

    if player_throw == "rock" and computer_throw == "scissors":
        print("\n"+"Rock beats scissors! You win the throw!"+"\n")
        time.sleep(1)
        return 1

    elif player_throw == "paper" and computer_throw == "rock":
        print("\n"+"Paper beats rock! You win the throw!"+"\n")
        time.sleep(1)
        return 1

    elif player_throw == "scissors" and computer_throw == "paper":
        print("\n"+"Scissors beat paper! You win the throw!"+"\n")
        time.sleep(1)
        return 1

    elif computer_throw == "rock" and player_throw == "scissors":
        print("\n"+"Rock beats scissors! Computer wins throw!"+"\n")
        time.sleep(1)
        return 2

    elif computer_throw == "paper" and player_throw == "rock":
        print("\n"+"Paper beats rock! Computer wins throw!"+"\n")
        time.sleep(1)
        return 2

    elif computer_throw == "scissors" and player_throw == "paper":
        print("\n"+"Scissors beat paper! Computer wins throw!"+"\n")
        time.sleep(1)
        return 2


while True:

    best_of = int(input("Play best of? "))

    print("\n"+"Ready?")
    time.sleep(1)
    print("Each of you raise your right fist and start the count, bringing your fists down on each count")
    time.sleep(2)

    player_wins = 0
    computer_wins = 0

    while True:
        print("1...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("\n"+"THROW!"+"\n")

        player_throw = str(input("You throw... "))
        while player_throw not in throws:
            print("You can only throw rock, paper or scissors, DUH!")
            player_throw = str(input("You throw..."))
        computer_throw = str((random.choice(throws)))
        print("Computer throws " + computer_throw.upper() + "!!")

        if player_throw == computer_throw:
            print("THROW AGAIN!!" + "\n")
            best_of += 1

        wins = throw_outcomes()

        if wins == 1:
            player_wins += 1
        elif wins == 2:
            computer_wins += 1

        best_of -= 1

        if computer_wins < player_wins > best_of:
            print("\n"+"YOU WIN!!!!"+"\n")
            break
        elif player_wins < computer_wins > best_of:
            print("\n"+"COMPUTER WINS!!!"+"\n")
            break
        else:
            continue

    play_again = input("Would you like to play again? Y/N ")
    print("\n")
    if play_again.upper() == "Y":
        continue
    else:
        print("\n"+"GAME OVER!!")
        break




