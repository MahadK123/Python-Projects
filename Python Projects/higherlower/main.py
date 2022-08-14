from art import logo, vs
from game_data import data 
import random 
score = 0 
game_over = False

# Generate random celeb
celeb_A = random.choice(data)
celeb_A_name = celeb_A['name']
celeb_A_desc = celeb_A['description']
celeb_A_loc = celeb_A['country']

def compare_celebs(celeb_A, celeb_B):

    if celeb_A > celeb_B:
        return 1
    else:
        return 0 

while game_over is False:
    print(logo)
    print(f"Compare A: {celeb_A_name}, a {celeb_A_desc}, from {celeb_A_loc}")
    print(vs)

    celeb_B = random.choice(data)
    celeb_B_name = celeb_B['name']
    celeb_B_desc = celeb_B['description']
    celeb_B_loc = celeb_B['country']
    print(f"Against B: {celeb_B_name}, a {celeb_B_desc}, from {celeb_B_loc}")

    ask_user = input("Who has more followers? Type 'A' or 'B': ").upper()
    celeb_A_score = celeb_A['follower_count']
    celeb_B_score = celeb_B['follower_count']

    if ask_user == 'A' and compare_celebs(celeb_A_score, celeb_B_score) == 0:
        print(f"Sorry, that's wrong Final score: {score}")
        game_over = True
    elif ask_user == 'B' and compare_celebs(celeb_A_score, celeb_B_score) == 1:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True
    elif score == 40:
        print(f"You win! Final score: {score}")
        game_over = True
    else:
        score += 1
        print(f"You're right! Current score: {score}.")
        celeb_A = celeb_B 
        celeb_A_name = celeb_B_name
        celeb_A_desc = celeb_B_desc
        Celeb_A_loc = celeb_B_loc