from random import randint
choices = ["paper", "scissors", "rock"]
playing_the_game = True
player = None
computer = None
keep_playing = None

while playing_the_game:

    print("\n...rock...\n...paper...\n...scissors...\nSHOOT!")

    player = input("\nPlayer 1's choice: ").lower()

    if player == 'quit' or player == 'q':
        playing_the_game = False
        print('\n\n')

    elif player != "rock" and player != "scissors" and player != "paper":
        print("\n\tIncorrect input!\n")

    else:
        computer = choices[randint(0, 2)]
        print(f"Computer plays {computer}\n")

        if player == computer:
            print("\n\tDraw!")
            
        elif player == "rock":
            if computer == "scissors": print("\n\tPlayer wins!")
            elif computer == "paper": print("\n\tComputer wins!")

        elif player == "scissors":
            if computer == "paper": print("\n\tPlayer wins!")
            elif computer == "rock": print("\n\tComputer wins!")

        elif player == "paper":
            if computer == "rock": print("\n\tPlayer wins!")
            elif computer == "scissors": print("\n\tComputer wins!")
        

        keep_playing = input('\n\tKeep playing? (y/n) ').lower()
        playing_the_game = keep_playing == 'y' or keep_playing == 'yes'
