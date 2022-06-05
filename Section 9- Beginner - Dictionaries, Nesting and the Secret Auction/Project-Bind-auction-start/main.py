from os import system
from pickle import FALSE, TRUE
from art import logo

print(logo)
print('Welcome to the secret auction program')

auctioner = {}
reset = FALSE

while reset:
    name = str(input('What is your name?: '))
    bid = int(input('What is your bid?: $'))
    another_one = input("Are there any other bidders? Type 'yes' or 'no'\n")
    auctioner[name] = bid
    system('cls')
    if another_one == "no":
        reset = FALSE

case = {
    "winner": "",
    'price': 0,
}
for man in auctioner:
    if auctioner[man] > case["price"]:
        case["price"] = auctioner[man]
        case["winner"] = man


print(f'winner is "{case["winner"]}" and price is {case["price"]}$')
