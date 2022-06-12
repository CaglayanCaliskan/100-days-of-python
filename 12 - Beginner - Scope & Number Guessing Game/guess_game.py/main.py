from art import logo
import random
print(logo)
print('Welcome to the Number Guessing Game!')

difficult = input("Choose a difficulty. Type 'easy' or 'hard': ")
global_attemps = 0
game_end = False


def difficult_select(dif):
    attemps = 0
    if dif == 'easy':
        attemps = 10
    else:
        attemps = 5
    return attemps


global_attemps = difficult_select(difficult)
game_number = random.randint(1, 100)


while not game_end:
    if global_attemps == 0:
        print('Game Over')
        print(f'Number was {game_number}')
        game_end = True
    else:
        print(
            f"You have a {global_attemps} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == game_number:
            print('You Win Boi')
            game_end = True
        elif guess > game_number:
            print('Too High')
            global_attemps -= 1
        else:
            print('Too Low')
            global_attemps -= 1
