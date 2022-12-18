
# try:
#     file = open('a_file.txt')
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
#     print("there was an error")
# except KeyError as error_message:
#     print("key error")
#     print(error_message)
# else:
#     content = file.read()
#     print(content)
# finally:
#     print("finally do it")
#     file.close()

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human not be over 3 metres")

bmi = weight / height**2
print(bmi)
