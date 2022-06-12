import random
from unicodedata import name
import art
from data import data
import os
print(art.logo)


# Global Variable
game_continue = True
score = 0

# Functions


def pick_data(list):
    return list[random.randint(0, (len(list)-1))]


def selected_print(obj, title):
    print(
        f"Compare {title}: {obj['name']}, {obj['description']}, from {obj['country']}  ")


def main(game_continue, compA, compB, score):
    while game_continue:
        selected_print(compA, 'A')
        print(f'kopya A: {compA["follower_count"]}')
        print(art.vs)
        selected_print(compB, 'B')
        print(f'kopya B: {compB["follower_count"]}')
        guess = input("Who has more followers? Type 'A' or 'B': ")
        if guess == 'A' and compA['follower_count'] > compB['follower_count'] or guess == 'B' and compB['follower_count'] > compA['follower_count']:
            compA = compB
            compB = pick_data(data)
            score += 1
            os.system('cls')
            print(f'Your Score is: {score}')
        else:
            print(f'Your Score is: {score}')
            print('GAME OVER')
            game_continue = False


# Game Pre Start
compA = pick_data(data)
compB = pick_data(data)
main(game_continue, compA, compB, score)
