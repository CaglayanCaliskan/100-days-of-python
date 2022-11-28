# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)


# with open("new_file.txt",  mode="w") as file:
#     file.write("\nNew text.")


# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


PLACE_HOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names_list = names_file.read().split()

with open('./Input/Lettes/starting_letter.txt') as letter_file:
    letter_content = letter_file.read()
    for name in names_list:
        new_letter = letter_content.replace(PLACE_HOLDER, name)
        with open(f"./Output/ReadyToSend/{name}_letter.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
