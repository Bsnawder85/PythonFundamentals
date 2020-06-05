from random import randint

# player must guess a number between 1 and 10.
random_number = randint(1, 10)
# gameplay flag. 
playing_the_game = True
keep_playing = ''
player_guess = None

while playing_the_game:
    player_guess = int(input('Guess a number between 1 and 10: '))

    # player guessed right, ask if game should continue
    if player_guess == random_number:

        print('\n\tYou guessed it! You Won!\n')
        keep_playing = input('\tDo you want to keep playing? (y/n) ').lower()

        playing_the_game = keep_playing == 'y' or keep_playing == 'yes'

        print('\n')
        # if the player wants to keep playing, pick another random number to guess
        if playing_the_game:
            random_number = randint(1, 10)

    elif player_guess > random_number:
        print('\nToo high, try again!')
    else:
        print('\nToo low, try again!')
