import random

## write 'hello world' to the console
#print('hello world')

# Player can enter one of the following commands:
# "rock", "paper", or "scissors"
# if the player enters an invalid command, the program will print "Invalid command"
# The computer will randomly select one of the three options
# The program will print the computer's choice
# The program will print the result of the game
# every round, the player will be asked if they want to play again
# if the player enters 'no', the program will print "Goodbye!" and exit
# if the player enters 'yes', the program will start a new round
# The program will keep track of the player's score and the computer's score
# The program will print the player's score and the computer's score after each round
# The program will print the final score after the player decides to stop playing
def play_game():
    player_score = 0
    computer_score = 0

    while True:
        # Player's turn
        player_choice = input("Enter 'rock', 'paper', or 'scissors': ")
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid command")
            continue

        # Computer's turn
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print("Computer's choice:", computer_choice)

        # Determine the winner
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            print("Player wins!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        # Print scores
        print("Player's score:", player_score)
        print("Computer's score:", computer_score)

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == 'no':
            break

    # Print final score
    print("Final score:")
    print("Player's score:", player_score)
    print("Computer's score:", computer_score)
    print("Goodbye!")

play_game()