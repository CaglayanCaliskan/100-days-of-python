# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
result = ""
for letter in range(0, int(nr_letters)):
    # random.choice(x) is simple way
    random_number = random.randint(0, len(letters)-1)
    result += letters[random_number]

for symbol in range(0, int(nr_symbols)):
    random_number = random.randint(0, len(symbols)-1)
    result += symbols[random_number]

for number in range(0, int(nr_numbers)):
    random_number = random.randint(0, len(numbers)-1)
    result += numbers[random_number]
print("Eazy Level: ", result)


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

list_of_result = list(result)
random.shuffle(list_of_result)
# i can loop for join but this s easier
string_of_result = "".join(list_of_result)

print("Hard Level: ", string_of_result)
