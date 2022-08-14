from art import logo
import random

def guessing_game():
    is_game_over = False
    
    # Check if user's answer is too high, too low, or correct
    def check_answer(answer, computer_number):
        if answer > computer_number:
            return "Too high."
        elif answer < computer_number:
            return "Too low."
        else:
            return 0
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or hard': ")
    
    # Set difficulty of the game 
    if difficulty == 'easy':
        num_guesses = 10
    else:
        num_guesses = 5

    computer_number = random.randint(1, 101)

    while is_game_over is False:
        print(f"You have {num_guesses} attempts remaining to guess the number.")
        answer = int(input("Make a guess: "))
        score = check_answer(answer, computer_number)
        if score == 0:
            print("You win!")
            is_game_over = True
        elif num_guesses == 0:
            print("You've run out of guesses, you lose!")
            is_game_over = True
        else:
            print(check_answer(answer, computer_number))
            print("Guess again.")
            print("")
            num_guesses -= 1
        

guessing_game()