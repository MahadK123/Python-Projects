############### Our Blackjack House Rules #####################



## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import random


# Get 2 random cards
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

# Calculate Score
def calculate_score(cards):
    score = sum(cards)
    # Check for blackjack
    if len(cards) == 2 and score == 21:
        return 0
    # Check for Ace, replace if 11
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return score

# Compare Score
def compare_score(user, computer):
    if user == 21:
        return "You win!"
    elif computer == 21:
        return "You lose!"
    elif user > 21:
        return "You lose!"
    elif computer > 21:
        return "You win!"
    elif user == computer:
        return "Draw"
    elif user < computer:
        return "You lose!"
    elif user > computer:
        return "You win!"


# Intro to game


def blackjack(user_input):
    user_cards = []
    computer_cards = []
    is_game_over = False
    if user_input == 'y':
        print(logo)
        for _ in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
        
        # Print user cards
        print(f"Your cards: {user_cards}")
        print(f"Computer's first card: {computer_cards[0]}")
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

    while is_game_over is False:
        # Game Over
        
            if user_score == 0 or computer_score == 0 or user_score > 21:
                is_game_over = True
            else:
                user_input = input("Type 'y' to get another card, type 'n' to pass: ")
                if user_input == 'y':
                    user_cards.append(deal_card())
                    print(f"Your cards: {user_cards}")
                    print(f"Computer's first card: {computer_cards[0]}")
                    user_score = calculate_score(user_cards)
                else:
                    is_game_over = True
                print(f"Your cards: {user_cards}")

            while computer_score != 0 and computer_score < 17:
                computer_cards.append(deal_card())
                computer_score = calculate_score(computer_cards)

    if is_game_over == True:
        print(compare_score(user_score, computer_score))
        print(f"Your final hand: {user_cards}")
        print(f"Computer's final hand: {computer_cards}")
        print("")     
        ask_user = input("Would you like to play again? Type 'y' or 'n': ")
        print("")
        # Re run the game
        if ask_user == 'y':
            blackjack(ask_user)
    
# Run the blackjack program
user_input = input("Would you like to play a game of blackjack? Type 'y' or 'n': ")

if user_input == 'y':
    blackjack('y')
