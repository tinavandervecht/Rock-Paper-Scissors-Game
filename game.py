from random import randint

choices = ["rock", "paper", "scissors"]
total_lives = 3
player_lives = total_lives
computer_lives = total_lives
player_choice = False

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
            global player_lives
            global computer_lives
            global total_lives

            player_lives = total_lives
            computer_lives = total_lives
        elif choice == "N" or choice == "n":
            # exit message and quit
            print("You chose to quit. Better luck next time!")
            exit()
        else:
            print("Make a valid choice - Y or N")
            choice = False

while player_choice is False:
    print("==================*/ RPS GAME */====================")
    print("Computer Lives:", computer_lives, "/", total_lives)
    print("Player Lives:", player_lives, "/", total_lives)
    print("====================================================")
    print("Choose your weapon! Or type quit to exit\n") #\n means "new line"
    player_choice = input("Choose rock, paper, or scissors: \n")

    if player_choice == "quit":
        print("You chose to quit")
        exit()

    computer_choice = choices[randint(0, 2)]

    print("user chose: " + player_choice)
    print("computer chose: " + computer_choice)

    if computer_choice == player_choice:
        print("tie")
    elif computer_choice == "rock":
        if player_choice == "scissors":
            player_lives -= 1
            print("you lose! player lives:", player_lives)
        else:
            print("you win!")
            computer_lives -= 1
    elif computer_choice == "paper":
        if player_choice == "rock":
            player_lives -= 1
            print("you lose! player lives:", player_lives)
        else:
            print("you win!")
            computer_lives -= 1
    elif computer_choice == "scissors":
        if player_choice == "paper":
            player_lives -= 1
            print("you lose! player lives:", player_lives)
        else:
            print("you win!")
            computer_lives -= 1

    if player_lives == 0:
        winorlose("lost")
    elif computer_lives == 0:
        winorlose("won")
    else:
        player_choice = False
