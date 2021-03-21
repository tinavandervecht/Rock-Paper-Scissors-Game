from random import randint

# re-import our game variables
from gameComponents import gameVars

# define a win / lose function and refer to it (invoke it) in our game loop
def winorlose(status):
    if status == "won":
        pre_message = "You are the huuuuuuugest winner ever! "
    else:
        pre_message = "You done trumped it, loser! "

    print(pre_message + 'Would you like to play again?')

    choice = False

    while choice == False:
        choice = input("Y / N? ")

        if choice == "Y" or choice == "y":
            # reset the game loop and start over again
            gameVars.player_lives = gameVars.total_lives
            gameVars.computer_lives = gameVars.total_lives
        elif choice == "N" or choice == "n":
            # exit message and quit
            print("You chose to quit. Better luck next time!")
            exit()
        else:
            print("Make a valid choice - Y or N")
            choice = False

while gameVars.player_choice is False:
    print("==================*/ RPS GAME */====================")
    print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
    print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
    print("====================================================")
    print("Choose your weapon! Or type quit to exit\n") #\n means "new line"
    gameVars.player_choice = input("Choose rock, paper, or scissors: \n")

    if gameVars.player_choice == "quit":
        print("You chose to quit")
        exit()

    gameVars.computer_choice = gameVars.choices[randint(0, 2)]

    print("user chose: " + gameVars.player_choice)
    print("computer chose: " + gameVars.computer_choice)

    if gameVars.computer_choice == gameVars.player_choice:
        print("tie")
    elif gameVars.computer_choice == "rock":
        if gameVars.player_choice == "scissors":
            gameVars.player_lives -= 1
            print("you lose! player lives:", gameVars.player_lives)
        else:
            print("you win!")
            gameVars.computer_lives -= 1
    elif gameVars.computer_choice == "paper":
        if gameVars.player_choice == "rock":
            gameVars.player_lives -= 1
            print("you lose! player lives:", gameVars.player_lives)
        else:
            print("you win!")
            gameVars.computer_lives -= 1
    elif gameVars.computer_choice == "scissors":
        if gameVars.player_choice == "paper":
            gameVars.player_lives -= 1
            print("you lose! player lives:", gameVars.player_lives)
        else:
            print("you win!")
            gameVars.computer_lives -= 1

    if gameVars.player_lives == 0:
        winorlose("lost")
    elif gameVars.computer_lives == 0:
        winorlose("won")
    else:
        gameVars.player_choice = False
