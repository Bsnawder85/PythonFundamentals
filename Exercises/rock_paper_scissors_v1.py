print("...rock...\n...paper...\n...scissors...")

player1_choice = input("Player 1's choice: ")
player2_choice = input("Player 2's choice: ")

print("SHOOT!")

if player1_choice == player2_choice:
    print("Draw!")
    
elif player1_choice == "rock":
    if player2_choice == "scissors": print("Player 1 wins!")
    elif player2_choice == "paper": print("Player 2 wins!")

elif player1_choice == "scissors":
    if player2_choice == "paper": print("Player 1 wins!")
    elif player2_choice == "rock": print("Player 2 wins!")

elif player1_choice == "paper":
    if player2_choice == "rock": print("Player 1 wins!")
    elif player2_choice == "scissors": print("Player 2 wins!")

# One or both players gave unexpected input
else:
    print("Incorrect input!")
