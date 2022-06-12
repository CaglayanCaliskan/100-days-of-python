import string
from art import ceasar_art


def ceasar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == 'decode':
        shift_amount *= -1

    for char in start_text:
        if char in alphabet:
            current_position_in_alphabet = alphabet.index(char)
            new_position = current_position_in_alphabet + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction} text is {end_text}")


print(ceasar_art)

alphabetz = list(string.ascii_lowercase)
alphabet = list(string.ascii_lowercase) + (alphabetz)

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    ceasar(start_text=text, shift_amount=shift, cipher_direction=direction)
    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print('GOODBYE')
